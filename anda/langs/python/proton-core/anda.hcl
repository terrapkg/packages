project pkg {
    arches = ["x86_64"]
  rpm {
    spec = "proton-core.spec"
  }
  labels {
    subrepo = "extras"
  }
}
