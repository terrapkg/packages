project "pkg" {
    rpm {
        spec = "nvidia-persistenced.spec"
    }
    labels = {
        subrepo = "nvidia"
    }
}