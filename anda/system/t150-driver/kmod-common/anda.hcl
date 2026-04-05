project pkg {
	arches = ["x86_64"]
	rpm {
		spec = "t150-driver.spec"
	}
	labels {
		nightly = 1
	}
}
