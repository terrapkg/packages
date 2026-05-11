project pkg {
    arches = ["x86_64"]
	rpm {
		spec = "rsms-inter-fonts.spec"
	}
	labels {
    subrepo = "extras"
    updbranch = 1
  }
}
