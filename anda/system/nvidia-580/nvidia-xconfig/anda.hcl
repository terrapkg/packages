project "pkg" {
    rpm {
        spec = "nvidia-xconfig-580.spec"
    }
    labels = {
        subrepo = "nvidia"
        weekly = 4
    }
}
