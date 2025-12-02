project pkg {
	arches = ["x86_64"]
	rpm {
		spec = "terra-release.spec"
	}
	labels {
		updbranch = 1
	}
}
