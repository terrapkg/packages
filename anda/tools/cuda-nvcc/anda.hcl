project "pkg" {
    rpm {
        spec = "cuda-nvcc.spec"
    }
    labels {
        upbranch = 1
        subrepo = "nvidia"
    }
}
