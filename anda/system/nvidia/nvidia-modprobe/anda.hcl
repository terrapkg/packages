project "pkg" {
    rpm {
        spec = "nvidia-modprobe.spec"
    }
    labels = {
        subrepo = "nvidia"
        group = "nvidia"
        weekly = 3
    }
}
