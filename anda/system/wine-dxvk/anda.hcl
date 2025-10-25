project pkg {
        arches = ["x86_64", "i386"]
	rpm {
		spec = "wine-dxvk.spec"
		extra_repos = ["https://repos.fyralabs.com/terrarawhide-mesa"]
	}
	labels {
	    mock = 1
	    subrepo = "extras"
	}
}
