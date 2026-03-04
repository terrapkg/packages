project "pkg" {
    rpm {
        spec = "cuda-nvcc.spec"
    }
    labels {
        updbranch = 1
        subrepo = "nvidia"
    }
}
