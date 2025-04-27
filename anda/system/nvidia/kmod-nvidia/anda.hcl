project pkg {
	rpm {
		spec = "kmod-nvidia.spec"
	}
	labels {
		subrepo = "nvidia"
		mock = 1
	}
}
