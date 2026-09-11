project pkg {
	arches = ["x86_64"]
	rpm {
		spec = "openrazer-kmod.spec"
	}
	labels {
		mock = 1
		updbranch = 1
	}
}
