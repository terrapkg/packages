project "pkg" {
    rpm {
        spec = "nvidia-modprobe-580xx.spec"
    }
    labels = {
        subrepo = "nvidia"
        weekly = 4
    }
}
