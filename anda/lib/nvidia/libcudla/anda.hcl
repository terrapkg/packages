project pkg {
    arches = ["aarch64"]
    rpm {
        spec = "libcudla.spec"
    }
    labels {
	    subrepo = "nvidia"
    }
}
