project pkg {
        arches = ["x86_64"]
	rpm {
		spec = "ryzen_smu.spec"
	}
	labels {
		nightly = 1
	}
}
