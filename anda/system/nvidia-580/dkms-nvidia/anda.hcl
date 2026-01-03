project pkg {
	rpm {
		spec = "dkms-nvidia-580.spec"
	}
	labels {
		subrepo = "nvidia"
		updbranch = 1
		mock = 1
	}
}
