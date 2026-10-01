project pkg {
	arches = ["x86_64"]
	rpm {
		spec = "ayaneo-leds.spec"
	}
	labels {
		nightly = 4
	}
}
