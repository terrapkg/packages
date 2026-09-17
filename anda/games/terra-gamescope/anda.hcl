project pkg {
    arches = ["x86_64", "aarch64", "i386"]
	rpm {
		spec = "terra-gamescope.spec"
	}
	labels {
		mock = 1
		quaterdaily = 1
		subrepo = "extras"
	}
}
