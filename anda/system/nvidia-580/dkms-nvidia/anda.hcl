project pkg {
	rpm {
		spec = "dkms-nvidia-580xx.spec"
	}
	labels {
		subrepo = "nvidia"
		group = "nvidia-580"
		updbranch = 1
		mock = 1
	}
}
