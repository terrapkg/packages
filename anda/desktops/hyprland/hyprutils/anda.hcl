project pkg {
  rpm {
    spec = "hyprutils.nightly.spec"
  }
  labels {
    nightly = 3
    subrepo = "extras"
  }
}
