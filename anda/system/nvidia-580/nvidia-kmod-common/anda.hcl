project "pkg" {
    rpm {
        spec = "nvidia-580-kmod-common.spec"
    }
    arches = ["x86_64"]
    labels = {
        subrepo = "nvidia"
        weekly = 4
    }
}
