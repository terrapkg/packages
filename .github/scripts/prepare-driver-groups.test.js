const assert = require("node:assert/strict");
const { test } = require("node:test");
const { execFileSync, spawnSync } = require("node:child_process");
const fs = require("node:fs");
const os = require("node:os");
const path = require("node:path");
const prepare = require("./prepare-driver-groups.js");
const { expandBuildMatrix, checkGroupVersions } = prepare;

const pkg = (name, group = "nvidia") => `anda/system/${group}/${name}/pkg`;
const manifest = {
  project: {
    [pkg("nvidia-driver")]: {
      arches: ["x86_64", "aarch64", "i386"],
      rpm: { spec: "driver.spec" }, labels: { mock: "1", subrepo: "nvidia" },
    },
    [pkg("nvidia-kmod-common")]: {
      arches: ["x86_64"], rpm: { spec: "common.spec" }, labels: { subrepo: "nvidia" },
    },
    [pkg("nvidia-container-toolkit")]: {
      rpm: { spec: "toolkit.spec" }, labels: { subrepo: "nvidia", no_upload_srpms: "1" },
    },
    [pkg("nvidia-driver", "nvidia-580")]: {
      arches: ["x86_64"], rpm: { spec: "legacy.spec" }, labels: { subrepo: "nvidia" },
    },
  },
};
const selected = (name, group) => ({ pkg: pkg(name, group), arch: "x86_64", labels: {} });

test("one selected driver expands to every configured package/architecture in its group", () => {
  const ordinary = { pkg: "anda/apps/example/pkg", arch: "aarch64", labels: { large: "1" } };
  const result = expandBuildMatrix([ordinary, selected("nvidia-driver")], manifest);
  assert.deepEqual(result.groups, ["nvidia"]);
  assert.equal(result.packages.length, 7);
  assert.deepEqual(result.packages[0], ordinary);
  assert.deepEqual(result.packages.filter((p) => p.pkg === pkg("nvidia-driver")).map((p) => p.arch),
    ["x86_64", "aarch64", "i386"]);
  assert.equal(result.packages.filter((p) => p.pkg === pkg("nvidia-kmod-common")).length, 1);
  assert.deepEqual(result.packages.filter((p) => p.pkg === pkg("nvidia-container-toolkit")).map((p) => p.arch),
    ["x86_64", "aarch64"]);
  assert.equal(result.packages.find((p) => p.pkg === pkg("nvidia-driver")).labels.mock, "1");
  assert.equal(result.packages.find((p) => p.pkg === pkg("nvidia-container-toolkit")).labels.no_upload_srpms, "1");
});

test("legacy and main groups expand independently and duplicate selections do not duplicate artifacts", () => {
  const legacy = selected("nvidia-driver", "nvidia-580");
  const result = expandBuildMatrix([legacy, legacy], manifest);
  assert.deepEqual(result.groups, ["nvidia-580"]);
  assert.equal(result.packages.length, 1);
  const both = expandBuildMatrix([selected("nvidia-driver"), legacy], manifest);
  assert.deepEqual(both.groups, ["nvidia", "nvidia-580"]);
  assert.equal(both.packages.length, 7);
});

test("unrelated NVIDIA-named packages do not trigger a driver group", () => {
  const entry = { pkg: "anda/system/nvidia-patch/pkg", arch: "x86_64", labels: {} };
  assert.deepEqual(expandBuildMatrix([entry], manifest), { packages: [entry], groups: [] });
  assert.deepEqual(expandBuildMatrix([], manifest), { packages: [], groups: [] });
});

test("invalid/empty driver groups and oversized matrices fail closed", () => {
  assert.throws(() => expandBuildMatrix([selected("missing")], manifest), /Unknown driver project/);
  assert.throws(() => expandBuildMatrix([selected("nvidia-driver")], { project: {} }), /No projects/);
  const emptyArches = { project: { [pkg("nvidia-driver")]: { rpm: {}, arches: [] } } };
  assert.throws(() => expandBuildMatrix([selected("nvidia-driver")], emptyArches), /No build architectures/);
  const oversized = { project: { [pkg("nvidia-driver")]: {
    rpm: {}, arches: Array.from({ length: 257 }, (_, i) => `arch-${i}`),
  } } };
  assert.throws(() => expandBuildMatrix([selected("nvidia-driver")], oversized), /256-job limit/);
});

test("version gate excludes independently versioned toolkit but rejects mismatched or unreadable drivers", async () => {
  const read = async (spec) => {
    assert.notEqual(spec, "toolkit.spec");
    return "615.1\n";
  };
  await checkGroupVersions(manifest, "nvidia", read);
  await assert.rejects(checkGroupVersions(manifest, "nvidia", async (spec) =>
    spec === "driver.spec" ? "615.1" : "615.0"), /Mismatched driver versions/);
  await assert.rejects(checkGroupVersions(manifest, "nvidia", async () => ""), /Expected one/);
  await assert.rejects(checkGroupVersions(manifest, "nvidia", async () => { throw new Error("bad spec"); }), /bad spec/);
  // Legacy version doesn't have to match the main driver's version.
  await checkGroupVersions(manifest, "nvidia-580", async () => "580.1");
});

test("prepare outputs full build list while blocking only the mismatched group", async () => {
  const previous = process.env.PACKAGES;
  process.env.PACKAGES = JSON.stringify([selected("nvidia-driver"), selected("nvidia-driver", "nvidia-580")]);
  const outputs = {};
  const warnings = [];
  try {
    await prepare({
      core: { setOutput: (k, v) => { outputs[k] = v; }, info: () => {}, warning: (v) => warnings.push(v) },
      exec: { getExecOutput: async (command, args) => {
        if (command === "anda") return { stdout: JSON.stringify(manifest) };
        assert.equal(command, "rpmspec");
        return { stdout: args.at(-1) === "driver.spec" ? "615.1" : "580.1" };
      } },
    });
  } finally {
    if (previous === undefined) delete process.env.PACKAGES;
    else process.env.PACKAGES = previous;
  }
  assert.equal(JSON.parse(outputs.packages).length, 7);
  assert.deepEqual(JSON.parse(outputs.blocked_groups), ["nvidia"]);
  assert.equal(warnings.length, 1);
});

// Execute the standalone publisher, replacing only the network CLI.
const workflow = fs.readFileSync(path.join(__dirname, "../workflows/nvidia-build.yml"), "utf8");
const regularWorkflow = fs.readFileSync(path.join(__dirname, "../workflows/json-build.yml"), "utf8");
const uploadBlock = workflow.split("      - name: Upload complete NVIDIA driver groups to subatomic\n")[1];
const uploadScriptPath = path.join(__dirname, "publish-nvidia.sh");

function runUpload(t, entries, { missingMarker, missingRpm, missingSource, blocked = [] } = {}) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "terra-driver-test-"));
  t.after(() => fs.rmSync(dir, { recursive: true, force: true }));
  fs.mkdirSync(path.join(dir, "bin"));
  const log = path.join(dir, "uploads.jsonl");
  const cli = path.join(dir, "bin/subatomic-cli");
  fs.writeFileSync(cli, `#!${process.execPath}\nrequire('node:fs').appendFileSync(process.env.UPLOAD_LOG, JSON.stringify(process.argv.slice(2))+'\\n');\n`);
  fs.chmodSync(cli, 0o755);
  for (const entry of entries) {
    const group = entry.pkg.includes("/nvidia-580/") ? "nvidia-580" : "nvidia";
    const name = `driver-${group}-${entry.pkg.replaceAll("/", "@")}\u002d${entry.arch}-rawhide`;
    const artifact = path.join(dir, "artifacts", name);
    for (const kind of ["rpms", "srpm"]) fs.mkdirSync(path.join(artifact, kind), { recursive: true });
    const basename = entry.pkg.replaceAll("/", "-");
    if (entry.pkg !== missingRpm) fs.writeFileSync(path.join(artifact, "rpms", `${basename}-${entry.arch}.rpm`), "");
    if (entry.pkg !== missingSource && entry.labels.no_upload_srpms !== "1") {
      fs.writeFileSync(path.join(artifact, "srpm", `${basename}.src.rpm`), "");
    }
    if (entry.pkg !== missingMarker) {
      const markerDir = path.join(dir, "artifacts", `ready-${name}`);
      fs.mkdirSync(markerDir);
      fs.writeFileSync(path.join(markerDir, "nvidia-build-success"), "");
    }
  }
  const result = spawnSync("bash", ["--noprofile", "--norc", uploadScriptPath], {
    cwd: dir, encoding: "utf8", env: {
      ...process.env, PACKAGES: JSON.stringify(entries), BLOCKED_GROUPS: JSON.stringify(blocked),
      VERSION: "rawhide", SUBATOMIC_TOKEN: "test-token", UPLOAD_LOG: log,
      PATH: `${path.join(dir, "bin")}:${process.env.PATH}`,
    },
  });
  const uploads = fs.existsSync(log) ? fs.readFileSync(log, "utf8").trim().split("\n").map(JSON.parse) : [];
  return { ...result, uploads };
}

test("full successful group uploads expanded filenames and honors source exclusion", (t) => {
  const entries = expandBuildMatrix([selected("nvidia-driver")], manifest).packages;
  const result = runUpload(t, entries);
  assert.equal(result.status, 0, result.stderr);
  assert.equal(result.uploads.length, 2);
  const [rpms, sources] = result.uploads;
  assert.equal(rpms.filter((arg) => arg.endsWith(".rpm")).length, 6);
  assert.equal(sources.filter((arg) => arg.endsWith(".rpm")).length, 2);
  assert.ok(result.uploads.flat().every((arg) => !arg.includes("*")));
  assert.ok(sources.every((arg) => !arg.includes("toolkit")));
});

for (const failure of ["missingMarker", "missingRpm", "missingSource"]) {
  test(`${failure} anywhere in the expanded group prevents its publication`, (t) => {
    const entries = expandBuildMatrix([selected("nvidia-driver")], manifest).packages;
    const result = runUpload(t, entries, { [failure]: pkg("nvidia-kmod-common") });
    assert.notEqual(result.status, 0);
    assert.deepEqual(result.uploads, []);
  });
}

test("healthy legacy group publishes even if main group failed or has mismatched versions", (t) => {
  const entries = expandBuildMatrix([selected("nvidia-driver"), selected("nvidia-driver", "nvidia-580")], manifest).packages;
  for (const options of [{ missingMarker: pkg("nvidia-kmod-common") }, { blocked: ["nvidia"] }]) {
    const result = runUpload(t, entries, options);
    assert.equal(result.status, 0, result.stderr);
    assert.equal(result.uploads.length, 2);
    assert.ok(result.uploads.flat().filter((arg) => arg.endsWith(".rpm")).every((arg) => arg.includes("nvidia-580")));
  }
});

test("NVIDIA workflow alone runs preparation and reuses the ordinary build steps", () => {
  assert.match(workflow, /packages: \$\{\{ needs.prepare.outputs.packages \}\}/);
  assert.match(workflow, /uses: \.\/\.github\/workflows\/json-build.yml/);
  assert.match(workflow, /driver_group: true/);
  assert.doesNotMatch(regularWorkflow, /prepare-driver-groups|needs: prepare|publish-nvidia:/);
  assert.match(regularWorkflow, /pkg: \$\{\{ fromJson\(inputs.packages\) \}\}/);
  assert.match(regularWorkflow, /if: inputs.publish && !inputs.driver_group/);
  assert.match(regularWorkflow, /if: inputs.driver_group && success\(\)/);
  assert.match(uploadBlock, /PACKAGES: \$\{\{ needs.prepare.outputs.packages \}\}/);
  assert.match(workflow, /needs: \[prepare, build\]/);
  assert.match(workflow, /needs.prepare.result == 'success'/);
  assert.match(uploadBlock, /shell: bash/);
  assert.match(uploadBlock, /run: bash \.github\/scripts\/publish-nvidia\.sh/);
  assert.doesNotMatch(uploadBlock, /run: \|/);
  const publisherSteps = workflow.split("  publish-nvidia:\n")[1];
  assert.ok(publisherSteps.indexOf("- name: Checkout") < publisherSteps.indexOf("- name: Download build artifacts"));
  execFileSync("bash", ["-n", uploadScriptPath]);
});

function splitMatrix(entries) {
  const output = execFileSync("jq", ["-r", "-f", path.join(__dirname, "split-build-matrix.jq")], {
    input: JSON.stringify(entries), encoding: "utf8",
  });
  return Object.fromEntries(output.trim().split("\n").map((line) => {
    const separator = line.indexOf("=");
    return [line.slice(0, separator), JSON.parse(line.slice(separator + 1))];
  }));
}

test("ordinary-only, driver-only, mixed, and empty inputs route without an extra preparation job", () => {
  const regular = { pkg: "anda/apps/example/pkg", arch: "x86_64", labels: {} };
  const patch = { pkg: "anda/system/nvidia-patch/pkg", arch: "x86_64", labels: {} };
  const current = selected("nvidia-driver");
  const legacy = selected("nvidia-driver", "nvidia-580");
  assert.deepEqual(splitMatrix([regular, patch]), { build_matrix: [regular, patch], nvidia_matrix: [] });
  assert.deepEqual(splitMatrix([current, legacy]), { build_matrix: [], nvidia_matrix: [current, legacy] });
  assert.deepEqual(splitMatrix([regular, current, legacy]), { build_matrix: [regular], nvidia_matrix: [current, legacy] });
  assert.deepEqual(splitMatrix([]), { build_matrix: [], nvidia_matrix: [] });
  for (const caller of ["autobuild.yml", "build.yml"]) {
    const yaml = fs.readFileSync(path.join(__dirname, "../workflows", caller), "utf8");
    assert.match(yaml, /if: needs.manifest.outputs.nvidia_matrix != '\[\]'/);
    assert.match(yaml, /if: needs.manifest.outputs.build_matrix != '\[\]'/);
    assert.match(yaml, /uses: \.\/\.github\/workflows\/nvidia-build.yml/);
    assert.match(yaml, /packages: \$\{\{ needs.manifest.outputs.nvidia_matrix \}\}/);
    assert.doesNotMatch(yaml, /prepare-driver-groups/);
  }
  const autobuild = fs.readFileSync(path.join(__dirname, "../workflows/autobuild.yml"), "utf8");
  assert.match(autobuild, /needs: \[build, nvidia\]/);
  assert.match(autobuild, /needs.nvidia.result == 'skipped'/);
});

test("custom builders and ordinary packages cannot bypass the full-group workflow", async () => {
  const previousPackages = process.env.PACKAGES;
  const previousBuilder = process.env.CUSTOM_BUILDER;
  try {
    process.env.PACKAGES = JSON.stringify([selected("nvidia-driver")]);
    process.env.CUSTOM_BUILDER = "x86-only-runner";
    await assert.rejects(prepare({}), /architecture-specific runners/);
    delete process.env.CUSTOM_BUILDER;
    process.env.PACKAGES = JSON.stringify([{ pkg: "anda/apps/example/pkg" }]);
    await assert.rejects(prepare({}), /ordinary build workflow/);
  } finally {
    if (previousPackages === undefined) delete process.env.PACKAGES;
    else process.env.PACKAGES = previousPackages;
    if (previousBuilder === undefined) delete process.env.CUSTOM_BUILDER;
    else process.env.CUSTOM_BUILDER = previousBuilder;
  }
  assert.match(workflow, /CUSTOM_BUILDER: \$\{\{ inputs.custom_builder \}\}/);
});

// Match actual names produced by the shared builder against the publisher's glob.
test("artifact patterns match both driver groups and their markers", () => {
  const script = regularWorkflow.split("      - name: Generating artifact name\n")[1]
    .split("        run: |\n")[1].split("\n\n")[0]
    .split("\n").map((line) => line.slice(10)).join("\n");
  const glob = workflow.match(/pattern: '([^']+)'/)[1];
  for (const [group, flag] of [["nvidia", "true"], ["nvidia-580", "true"], ["nvidia", "false"]]) {
    const substituted = script.replaceAll("${{ matrix.pkg.pkg }}", pkg("nvidia-driver", group))
      .replaceAll("${{ matrix.pkg.arch }}", "x86_64")
      .replaceAll("${{ matrix.version }}", "rawhide")
      .replaceAll("${{ inputs.driver_group }}", flag)
      .replace('>> $GITHUB_OUTPUT', '');
    const name = execFileSync("bash", ["-e", "-c", substituted], { encoding: "utf8" }).trim().slice(5);
    if (flag === "true") {
      assert.ok(name.startsWith(`driver-${group}-`));
      for (const artifact of [name, `ready-${name}`]) {
        execFileSync("bash", ["-c", '[[ "$1" == $2 ]]', "test", artifact, glob]);
      }
    } else {
      assert.ok(!name.startsWith("driver-"));
    }
  }
});
