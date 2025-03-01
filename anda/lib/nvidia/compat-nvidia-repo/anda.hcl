project pkg {
    arches = ["x86_64"]
        rpm {
		spec = "compat-nvidia-repo.spec"
	}
	labels {
	   subrepo = "nvidia"
    }
}
