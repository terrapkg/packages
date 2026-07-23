project pkg {
   arches = ["x86_64"]
    rpm {
        spec = "cuda-profiler.spec"
    }
    labels {
        mock = 1
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
