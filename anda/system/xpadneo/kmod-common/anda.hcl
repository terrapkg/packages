project pkg {
        arches = ["x86_64"]
	rpm {
		spec = "xpadneo-kmod-common.spec"
	}
	labels {
		mock = 1
		nightly = 1
	}
}
