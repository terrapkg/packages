project "pkg" {
    rpm {
        spec = "nvidia-xconfig.spec"
    }
    labels = {
        subrepo = "nvidia"
        group = "nvidia"
        weekly = 3
    }
}
