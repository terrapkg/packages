project pkg {
        arches = ["x86_64"]
    rpm {
        spec = "cuda-nvprof.spec"
    }
    labels {
	    subrepo = "nvidia"
    }
}
