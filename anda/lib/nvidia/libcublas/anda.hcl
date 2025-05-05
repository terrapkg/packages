project pkg {
    rpm {
        spec = "libcublas.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
