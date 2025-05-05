project pkg {
    rpm {
        spec = "libcurand.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
