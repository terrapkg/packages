project "pkg" {
    rpm {
        spec = "nvidia-open-kmod.spec"
    }
    labels {
        mock = 1
        subrepo = "nvidia"
    }
}
