project pkg {
        arches = ["x86_64"]
    rpm {
        spec = "nv-codec-headers.spec"
    }
    labels {
	    subrepo = "nvidia"
    }
}
