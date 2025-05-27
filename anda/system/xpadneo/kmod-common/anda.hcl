project pkg {
        arches = ["x86_64"]
	rpm {
		spec = "xpadneo.spec"
	}
	labels {
		nightly = 1
	}
}
