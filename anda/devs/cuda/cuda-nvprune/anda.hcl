project pkg {
    rpm {
        spec = "cuda-nvprune.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
