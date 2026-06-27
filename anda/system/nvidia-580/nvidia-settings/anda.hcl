project "pkg" {
    rpm {
        spec = "nvidia-settings-580.spec"
    }
    labels = {
        subrepo = "nvidia"
        weekly = 4
    }
}
