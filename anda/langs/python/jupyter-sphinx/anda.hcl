project pkg {
    arches = ["x86_64"]
  rpm {
	spec = "python-jupyter-sphinx.spec"
  }
  labels {
    subrepo = "extras"
  }
}
