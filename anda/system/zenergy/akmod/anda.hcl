project pkg {
        arches = ["x86_64"]
	rpm {
		spec = "zenergy-kmod.spec"
	}
	labels {
		nightly = 1
	}
}
