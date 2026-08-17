project pkg {
        arches = ["x86_64"]
	rpm {
		spec = "xpad-noone.spec"
	}
	labels {
	    nightly = 1
	}
}
