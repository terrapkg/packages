const GROUPS = ["nvidia", "nvidia-580"];
// Match anda ci's default when a project has no explicit arches.
const DEFAULT_ARCHES = ["x86_64", "aarch64"];

function driverGroup(pkg) {
  return GROUPS.find((group) => pkg.startsWith(`anda/system/${group}/`));
}

function expandBuildMatrix(packages, manifest) {
  const groups = GROUPS.filter((group) =>
    packages.some((entry) => driverGroup(entry.pkg) === group),
  );
  const expanded = packages.filter((entry) => !driverGroup(entry.pkg));
  for (const group of groups) {
    const projects = Object.entries(manifest.project).filter(
      ([pkg]) => driverGroup(pkg) === group,
    );
    if (!projects.length) throw new Error(`No projects found for ${group}`);
    for (const entry of packages.filter((entry) => driverGroup(entry.pkg) === group)) {
      if (!manifest.project[entry.pkg]) {
        throw new Error(`Unknown driver project: ${entry.pkg}`);
      }
    }
    for (const [pkg, project] of projects) {
      if (!project.rpm) throw new Error(`Driver project is not an RPM build: ${pkg}`);
      const arches = project.arches ?? DEFAULT_ARCHES;
      if (!arches.length) throw new Error(`No build architectures for ${pkg}`);
      for (const arch of arches) {
        expanded.push({ pkg, arch, labels: project.labels ?? {} });
      }
    }
  }
  // Never allow duplicate entries to collide on artifact names.
  const unique = [...new Map(expanded.map((entry) => [
    JSON.stringify([entry.pkg, entry.arch]), entry,
  ])).values()];
  if (unique.length > 256) throw new Error("Expanded build matrix exceeds GitHub's 256-job limit");
  return { packages: unique, groups };
}

async function checkGroupVersions(manifest, group, getVersion) {
  const versions = [];
  for (const [pkg, project] of Object.entries(manifest.project)) {
    if (driverGroup(pkg) !== group) continue;
    // Container toolkit has its own release cycle, not the driver version.
    if (pkg === `anda/system/${group}/nvidia-container-toolkit/pkg`) continue;
    const version = (await getVersion(project.rpm.spec)).trim();
    if (!version || version.includes("\n")) {
      throw new Error(`Expected one source package version for ${pkg}`);
    }
    versions.push([pkg, version]);
  }
  if (!versions.length) throw new Error(`No driver versions found for ${group}`);
  if (new Set(versions.map(([, version]) => version)).size !== 1) {
    throw new Error(`Mismatched driver versions in ${group}:\n${versions.map(
      ([pkg, version]) => `  ${pkg}: ${version}`,
    ).join("\n")}`);
  }
}

module.exports = async ({ core, exec }) => {
  const packages = JSON.parse(process.env.PACKAGES);
  if (!Array.isArray(packages)) throw new Error("PACKAGES must be an array");
  if (process.env.CUSTOM_BUILDER) {
    throw new Error("Full driver groups require architecture-specific runners; custom_builder is not supported");
  }
  if (packages.some((entry) => !driverGroup(entry.pkg))) {
    throw new Error("Use the ordinary build workflow for packages outside the NVIDIA driver folders");
  }
  const touched = packages.some((entry) => driverGroup(entry.pkg));
  const manifest = touched
    ? JSON.parse((await exec.getExecOutput("anda", ["run", "andax/ci/manifest.rhai"], {
      silent: true,
    })).stdout)
    : { project: {} };
  const expanded = expandBuildMatrix(packages, manifest);
  const blockedGroups = [];
  for (const group of expanded.groups) {
    try {
      await checkGroupVersions(manifest, group, async (spec) => (
        await exec.getExecOutput("rpmspec", ["-q", "--srpm", "--qf", "%{VERSION}\n", spec], {
          silent: true,
        })
      ).stdout);
    } catch (error) {
      core.warning(`Not publishing ${group}: ${error.message}`);
      blockedGroups.push(group);
    }
  }
  core.info(`Expanded ${packages.length} selected builds to ${expanded.packages.length} builds`);
  core.setOutput("packages", JSON.stringify(expanded.packages));
  core.setOutput("blocked_groups", JSON.stringify(blockedGroups));
};

module.exports.expandBuildMatrix = expandBuildMatrix;
module.exports.checkGroupVersions = checkGroupVersions;
