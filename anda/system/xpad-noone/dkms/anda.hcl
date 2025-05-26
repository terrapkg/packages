project pkg {
        arches = ["x86_64"]
	rpm {
		spec = "dkms-xpad-noone.spec"
	}
	labels {
		mock = 1
		updbranch = 1
	}
}
