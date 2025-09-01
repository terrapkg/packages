project pkg {
	rpm {
		spec = "kf6-kio.spec"
	}
	labels {
		subrepo = "extras"
		updbranch = 1
                mock = 1
	}
}
