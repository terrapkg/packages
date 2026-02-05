project "pkg" {
    arches = ["x86_64"]
    rpm {
        spec = "twintaillauncher.spec"
        mock = 1
    }
}
