project "pkg" {
    rpm {
        spec = "nvidia-modprobe-580.spec"
    }
    labels = {
        subrepo = "nvidia"
        weekly = 4
    }
}
