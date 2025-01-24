project "pkg" {
    rpm {
        spec = "nvidia-settings.spec"
    }
    labels = {
        subrepo = "nvidia"
    }
}