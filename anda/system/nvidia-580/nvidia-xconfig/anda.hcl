project "pkg" {
    rpm {
        spec = "nvidia-xconfig-580xx.spec"
    }
    labels = {
        subrepo = "nvidia"
        group = "nvidia-580"
        weekly = 4
    }
}
