project pkg {
  	arches = ["aarch64"]
	rpm {
		spec = "rpi-update.spec"
	}
	labels {
	   nightly = 1
	}
}
