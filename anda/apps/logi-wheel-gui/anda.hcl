project pkg {
  arches = ["x86_64"]
  rpm {
    spec = "logi-wheel-gui.spec"
  }
  labels {
      updbranch = 1
      mock = 1
  }
}
