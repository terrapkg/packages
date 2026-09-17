project "pkg" {
    rpm {
        spec = "nvidia-580xx-kmod.spec"
    }
    labels {
        mock = 1
        subrepo = "nvidia"
        updbranch = 1
    }
}
