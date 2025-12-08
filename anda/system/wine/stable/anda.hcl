project pkg {
        arches = ["x86_64", "aarch64"]
	rpm {
		spec = "wine-stable.spec"
		extra_repos = ["https://repos.fyralabs.com/terra\\$releasever-mesa"]
	}
	labels {
	    mock = 1
	    subrepo = "extras"
	}
}
