project pkg {
	arches = ["x86_64", "aarch64"]
	rpm {
		spec = "herdr.spec"
	}
	labels {
		large = 1
	}
}
