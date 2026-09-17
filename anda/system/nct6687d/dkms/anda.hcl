project pkg {
        arches = ["x86_64"]
	rpm {
		spec = "dkms-nct6687d.spec"
	}
	labels {
		updbranch = 1
		mock = 1
	}
}
