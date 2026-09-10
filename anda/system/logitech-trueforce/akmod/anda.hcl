project pkg {
	arches = ["x86_64"]
	rpm {
		spec = "logitech-trueforce-kmod.spec"
	}
	labels {
		mock = 1
		updbranch = 1
	}
}
