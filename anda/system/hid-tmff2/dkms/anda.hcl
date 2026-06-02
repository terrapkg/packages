project pkg {
	arches = ["x86_64"]
	rpm {
		spec = "dkms-hid-tmff2.spec"
	}
	labels {
		mock = 1
		updbranch = 1
	}
}
