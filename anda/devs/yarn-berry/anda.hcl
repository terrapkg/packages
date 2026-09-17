project pkg {
        arches = ["x86_64"]
	rpm {
		spec = "yarnpkg-berry.spec"
	}
	labels {
	    subrepo = "extras"
	}
}
