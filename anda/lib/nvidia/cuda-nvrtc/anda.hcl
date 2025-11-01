project pkg {
    rpm {
        spec = "cuda-nvrtc.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
