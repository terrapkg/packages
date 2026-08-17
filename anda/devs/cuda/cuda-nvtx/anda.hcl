project pkg {
    rpm {
        spec = "cuda-nvtx.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
