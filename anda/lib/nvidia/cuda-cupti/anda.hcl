project pkg {
    rpm {
        spec = "cuda-cupti.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
