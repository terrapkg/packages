project pkg {
  rpm {
    spec = "xdg-desktop-portal-umbriel.spec"
  }
  labels {
    // this package needs to have this name but is still nightly for now
    nightly = 1
  }
}
