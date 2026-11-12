project pkg {
	arches = ["x86_64"]
	rpm {
		spec = "ayaneo-platform-kmod.spec"
	}
	labels {
		mock = 1
	}
}
