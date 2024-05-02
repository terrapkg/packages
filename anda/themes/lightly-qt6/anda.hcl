project "pkg" {
    arches = ["x86_64", "aarch64"]
    rpm {
        spec = "lightly-qt6.spec"
    }
}
