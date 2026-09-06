project pkg {
	arches = ["x86_64"]
	rpm {
		spec = "logitech-rs50-linux-driver.spec"
	}
	labels {
		nightly = 1
	}
}
