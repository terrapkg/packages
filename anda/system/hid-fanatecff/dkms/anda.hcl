project pkg {
	arches = ["x86_64"]
	rpm {
		spec = "dkms-hid-fanatecff.spec"
	}
	labels {
		mock = 1
		updbranch = 1
	}
}
