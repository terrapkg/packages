project pkg {
        arches = ["x86_64"]
	rpm {
		spec = "dkms-zenergy.spec"
	}
	labels {
		nightly = 1
	}
}
