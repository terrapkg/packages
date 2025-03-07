project pkg {
        arches = ["x86_64"]
	rpm {
		spec = "xpadneo-kmod-common.spec"
	}
	labels {
		nightly = 1
	}
}
