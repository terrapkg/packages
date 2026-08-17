project pkg {
    rpm {
        spec = "cuda-tileiras.spec"
    }
    labels {
        mock = 1
        subrepo = "nvidia"
        updbranch = 1
    }
}
