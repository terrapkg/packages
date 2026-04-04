project pkg {
        arches = ["x86_64"]
	rpm {
		spec = "dkms-logitech-rs50-linux-driver.spec"
	}
	labels {
		nightly = 1
	}
}
