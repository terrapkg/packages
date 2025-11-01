project pkg {
    rpm {
        spec = "libcufft.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
