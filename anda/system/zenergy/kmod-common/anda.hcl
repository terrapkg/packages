project pkg {
        arches = ["x86_64"]
	rpm {
		spec = "zenergy.spec"
	}
	labels {
		nightly = 1
	}
}
