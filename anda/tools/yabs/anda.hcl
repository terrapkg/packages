project pkg {
    arches = ["x86_64"]
	rpm {
		spec = "yabs.spec"
	}
	labels {
		nightly = 1
	}
}
