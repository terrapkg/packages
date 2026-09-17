project "pkg" {
    rpm {
        spec = "nvidia-xconfig-580xx.spec"
    }
    labels = {
        subrepo = "nvidia"
        weekly = 4
    }
}
