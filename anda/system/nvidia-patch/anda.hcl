project "pkg" {
    rpm {
        spec = "nvidia-patch.spec"
    }
   	labels {
		nightly = 2
                subrepo = "nvidia"
	}
}
