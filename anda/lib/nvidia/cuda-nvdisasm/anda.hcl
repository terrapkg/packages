project pkg {
    rpm {
        spec = "cuda-nvdisasm.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
