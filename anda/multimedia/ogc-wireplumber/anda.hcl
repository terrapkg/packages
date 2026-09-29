project pkg {
  rpm {
    spec = "ogc-wireplumber.spec"
  }

  labels {
    mock = 1
    subrepo = "extras"
  }
}
