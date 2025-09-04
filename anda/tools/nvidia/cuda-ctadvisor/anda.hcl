project "pkg" {
    rpm {
        spec = "cuda-ctadvisor.spec"
    }
    labels {
        updbranch = 1
        subrepo = "nvidia"
    }
}
