project "pkg" {
    rpm {
        spec = "nvidia-kmod-common.spec"
    }
    arches = ["x86_64"]
    labels = {
        subrepo = "nvidia"
    }
}