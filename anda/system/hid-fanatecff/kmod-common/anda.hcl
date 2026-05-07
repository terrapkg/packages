project pkg {
	arches = ["x86_64"]
	rpm {
		spec = "hid-fanatecff.spec"
	}
	labels {
		nightly = 1
	}
}
