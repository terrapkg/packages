project pkg {
  arches = ["x86_64"]
  rpm {
    spec = "hyprland-protocols.nightly.spec"
  }
  labels {
    nightly = 2
    subrepo = "extras"
  }
}
