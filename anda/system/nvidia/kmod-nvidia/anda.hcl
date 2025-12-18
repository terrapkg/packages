project pkg {
	rpm {
		spec = "kmod-nvidia.spec"
	}
	labels {
		subrepo = "nvidia"
		mock = 1
		updbranch = 1
	}
}
