let result = sh("dnf repoquery --available --qf '%{name}' bazel 2>/dev/null | grep -qx bazel", #{
    "stdout": "null",
    "stderr": "null",
});

if result.ctx.rc == 0 {
    print("Bazel is available in the configured repositories; using it as a build dependency");
    rpm.global("bootstrap", "0");
} else {
    print("Bazel is not available in the configured repositories; bootstrapping it");
}
