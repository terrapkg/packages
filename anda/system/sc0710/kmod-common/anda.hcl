project pkg {
        arches = ["x86_64"]
	rpm {
		spec = "sc0710.spec"
	}
	labels {
		nightly = 1
	}
}
