project pkg {
	arches = ["x86_64"]
	rpm {
		spec = "terra-gpg-keys.spec"
	}
	labels {
		updbranch = 1
	}
}
