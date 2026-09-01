project pkg {
	arches = ["x86_64"]
	rpm {
		spec = "openrazer.spec"
	}
	labels {
		nightly = 1
	}
}
