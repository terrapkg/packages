project pkg {
               arches = ["x86_64"]
	rpm {
		spec = "xone-nightly.spec"
	}
	labels {
                nightly = 1
	}
}
