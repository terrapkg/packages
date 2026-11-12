project pkg {
	rpm {
		spec = "dkms-nvidia.spec"
	}
	labels {
		subrepo = "nvidia"
		group = "nvidia"
    updbranch = 1
    mock = 1
	}
}
