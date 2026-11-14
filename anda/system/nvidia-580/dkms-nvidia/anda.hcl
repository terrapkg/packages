project pkg {
	rpm {
		spec = "dkms-nvidia-580xx.spec"
	}
	labels {
		subrepo = "nvidia"
		group = "nvidia-580"
		weekly = 4
		mock = 1
	}
}
