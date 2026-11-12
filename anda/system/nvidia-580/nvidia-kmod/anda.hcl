project "pkg" {
    rpm {
        spec = "nvidia-580xx-kmod.spec"
    }
    labels {
        mock = 1
        subrepo = "nvidia"
        group = "nvidia-580"
        updbranch = 1
    }
}
