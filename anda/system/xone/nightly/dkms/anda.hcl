project pkg {
               arches=["x86_64"]
	rpm {
		spec = "dkms-xone-nightly.spec"
	}
	labels {
		mock = 1
		updbranch = 1
	}
}
