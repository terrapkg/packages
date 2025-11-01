project pkg {
	rpm {
		spec = "dkms-nvidia-open.spec"
	}
	labels {
		subrepo = "nvidia"
        weekly = 1
	}
}
