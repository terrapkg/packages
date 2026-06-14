project "pkg" {
        arches = ["x86_64"]
    rpm {
        spec = "nvidia-580-kmod-common.spec"
    }
    labels = {
        subrepo = "nvidia"
        updbranch = 1
    }
}
