project pkg {
    rpm {
        spec = "cuda-cudart.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
