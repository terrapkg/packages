project pkg {
    rpm {
        spec = "cuda-cudnn.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
