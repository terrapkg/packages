project "pkg" {
    rpm {
        spec = "nvidia-settings.spec"
    }
    labels = {
        subrepo = "nvidia"
        group = "nvidia"
        weekly = 3
    }
}
