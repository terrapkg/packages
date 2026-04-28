project "pkg" {
    rpm {
        spec = "nvidia-persistenced-580.spec"
    }
    labels = {
        subrepo = "nvidia"
        weekly = 4
    }
}
