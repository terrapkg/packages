project pkg {
        arches = ["x86_64"]
	rpm {
		spec = "zenergy-kmod.spec"
	}
	labels {
		mock = 1
		nightly = 1
	}
}
