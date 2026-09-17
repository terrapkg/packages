project "pkg" {
        arches = ["x86_64"]
    rpm {
        spec = "nvidia-kmod-common.spec"
    }
    labels = {
        subrepo = "nvidia"
        updbranch = 1
    }
}
