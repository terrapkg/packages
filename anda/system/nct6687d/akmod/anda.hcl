project pkg {
	arches = ["x86_64"]
	rpm {
		spec = "nct6687d-kmod.spec"
	}
	labels {
		mock = 1
		updbranch = 1
	}
}
