project "pkg" {
    rpm {
        spec = "cuda-crt.spec"
    }
    labels {
        updbranch = 1
        subrepo = "nvidia"
    }
}
