project pkg {
               arches = ["x86_64"]
	rpm {
		spec = "xonedo-nightly.spec"
	}
	labels {
                nightly = 1
	}
}
