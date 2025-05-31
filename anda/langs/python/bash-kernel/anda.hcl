project pkg {
    arches = ["x86_64"]
  rpm {
	spec = "python-bash-kernel.spec"
  }
  labels {
    subrepo = "extras"
  }
}
