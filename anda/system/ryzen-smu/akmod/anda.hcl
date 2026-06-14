project pkg {
        arches = ["x86_64"]
	rpm {
		spec = "ryzen_smu-kmod.spec"
	}
	labels {
		mock = 1
		nightly = 1
	}
}
