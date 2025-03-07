project pkg {
               arches = ["x86_64"]
	rpm {
		spec = "xone.spec"
	}
	labels {
                nightly = 1
	}
}
