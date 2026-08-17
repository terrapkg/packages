project pkg {
	arches = ["x86_64"]
	rpm {
		spec = "logitech-rs50-linux-driver-kmod.spec"
	}
	labels {
		mock = 1
		updbranch = 1
	}
}
