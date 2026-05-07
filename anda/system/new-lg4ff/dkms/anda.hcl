project pkg {
	arches = ["x86_64"]
	rpm {
		spec = "dkms-new-lg4ff.spec"
	}
	labels {
		mock = 1
		updbranch = 1
	}
}
