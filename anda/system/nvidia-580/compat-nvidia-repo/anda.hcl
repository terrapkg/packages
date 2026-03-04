project pkg {
    arches = ["x86_64"]
        rpm {
		spec = "compat-nvidia-repo-580.spec"
	}
	labels {
	   subrepo = "nvidia"
	   weekly = 4
    }
}
