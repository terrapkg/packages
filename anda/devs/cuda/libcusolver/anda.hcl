project pkg {
    rpm {
        spec = "libcusolver.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
