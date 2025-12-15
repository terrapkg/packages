project "pkg" {
    rpm {
        spec = "nvidia-kmod-common-580.spec"
    }
    arches = ["x86_64"]
    labels = {
        subrepo = "nvidia"
        weekly = 4
    }
}
