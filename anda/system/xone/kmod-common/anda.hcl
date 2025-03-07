project pkg {
               arches = ["x86_64"]
	rpm {
		spec = "xone.spec"
	}
	labels {
		mock = 1
                nightly = 1
	}
}
