project "pkg" {
    rpm {
        spec = "nvidia-settings-580xx.spec"
    }
    labels = {
        subrepo = "nvidia"
        weekly = 4
    }
}
