project pkg {
    arches = ["x86_64"]
	rpm {
		spec = "geteltorito.spec"
	}
	labels {
	   nightly = 1
	}
}