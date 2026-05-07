project pkg {
               arches=["x86_64"]
	rpm {
		spec = "dkms-xonedo.spec"
	}
	labels {
		mock = 1
		updbranch = 1
	}
}
