project pkg {
   arches = ["x86_64", "aarch64", "i386"]
    rpm {
        spec = "cuda-profiler.spec"
    }
    labels {
        mock = 1
	    subrepo = "nvidia"
    }
}
