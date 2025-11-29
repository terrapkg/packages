project pkg {
	arches = ["x86_64"]
	rpm {
		spec = "udev-joystick-blacklist.spec"
	}
	labels {
		nightly = 1
	}
}
