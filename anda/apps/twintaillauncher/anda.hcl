project "pkg" {
    arches = ["x86_64"]
    mock = 1
    rpm {
        spec = "twintaillauncher.spec"
    }
}
