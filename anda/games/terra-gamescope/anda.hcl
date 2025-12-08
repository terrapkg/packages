project pkg {
    arches = ["x86_64", "aarch64"]
	rpm {
		spec = "terra-gamescope.spec"
	}
	labels {
		mock = 1
		subrepo = "extras"
	}
}
