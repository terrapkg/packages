project "pkg" {
        arches = ["aarch64"]
    rpm {
        spec = "python-toml-cli.spec"
    }
    labels {
        updbranch = 1
    }
}
