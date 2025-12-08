project pkg {
        arches = ["x86_64"]
	rpm {
		spec = "wine-dxvk.spec"
	}
	labels {
	    mock = 1
	    subrepo = "extras"
	}
}
