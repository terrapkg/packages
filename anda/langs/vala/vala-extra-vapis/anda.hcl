project pkg {
    arches = ["aarch64"]
	rpm {
		spec = "vala-extra-vapis.spec"
	}
	labels {
		mock = 1
	}
}
