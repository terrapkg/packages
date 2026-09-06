project pkg {
        arches = ["x86_64"]
	rpm {
		spec = "xpadneo-nightly.spec"
	}
	labels {
		nightly = 1
	}
}
