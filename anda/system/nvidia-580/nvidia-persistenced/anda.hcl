project "pkg" {
    rpm {
        spec = "nvidia-persistenced-580xx.spec"
    }
    labels = {
        subrepo = "nvidia"
        weekly = 4
    }
}
