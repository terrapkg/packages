project pkg {
    arches = ["x86_64"]
	rpm {
		spec = "sidepulse.spec"
	}
	labels {
		nightly = 2
	}
}
