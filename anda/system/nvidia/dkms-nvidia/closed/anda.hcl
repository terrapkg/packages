project pkg {
	rpm {
		spec = "dkms-nvidia.spec"
	}
	labels {
		subrepo = "nvidia"
		updbranch = 1
    mock = 1
	}
}
