project "pkg" {
    rpm {
        spec = "nvidia-xconfig.spec"
    }
    labels = {
        subrepo = "nvidia"
        weekly = 3
    }
}
