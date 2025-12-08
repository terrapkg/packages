project pkg {
        arches = ["x86_64", "aarch64"]
	rpm {
		spec = "wine-staging.spec"
	}
	labels {
	    mock = 1
	    subrepo = "extras"
	}
}
