project pkg {
    arches = ["x86_64"]
        rpm {
	    spec = "cuda-gcc.spec"
	}
    labels {
        updbranch = 1
        subrepo = "nvidia"
    }
}
