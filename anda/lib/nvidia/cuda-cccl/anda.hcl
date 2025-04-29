project pkg {
    rpm {
        spec = "cuda-cccl.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
