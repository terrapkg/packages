project pkg {
    rpm {
        spec = "cuda-sandbox.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
