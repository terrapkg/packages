project pkg {
        arches = ["x86_64"]
	rpm {
		spec = "pokeshell.spec"
	}
	labels {
	    nightly = 1
	}
}
