project pkg {
	rpm {
		spec = "dkms-nvidia.spec"
	}
	labels {
		subrepo = "nvidia"
		group = "nvidia"
    weekly = 3
    mock = 1
	}
}
