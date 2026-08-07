project pkg {
	arches = ["x86_64"]
	rpm {
		spec = "hid-tmff2.spec"
	}
	labels {
		nightly = 1
	}
}
