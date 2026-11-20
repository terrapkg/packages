project pkg {
    arches = ["x86_64"]
        rpm {
		spec = "compat-nvidia-repo-580xx.spec"
	}
	labels {
	   subrepo = "nvidia"
	   group = "nvidia-580"
	   weekly = 4
    }
}
