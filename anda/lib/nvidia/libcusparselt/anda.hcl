project pkg {
    rpm {
        spec = "libcusparselt.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
