project pkg {
        arches = ["x86_64"]
	rpm {
		spec = "dkms-logitech-trueforce.spec"
	}
	labels {
		mock = 1
		updbranch = 1
	}
}
