project pkg {
    arches = ["x86_64", "aarch64"]
    rpm {
        spec = "terra-fcitx5-mozc.spec"
    }
    labels {
        mock = 1
        subrepo = "extras"
    }
}
