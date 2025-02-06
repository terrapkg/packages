project pkg {
    arches = ["x86_64", "aarch64", "i386"]
	rpm {
		spec = "terra-extras-gamescope.spec"
	}
	labels {
		mock = 1
		subrepo = "extras"
	}
}
