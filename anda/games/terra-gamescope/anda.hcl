project pkg {
    arches = ["x86_64", "aarch64", "i386"]
	rpm {
		spec = "terra-gamescope.spec"
	}
	labels {
		extra = 1
	}
}
