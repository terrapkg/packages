project pkg {
  arches = ["x86_64"]

  rpm {
    spec = "kernel-surface.spec"
  }
  labels {
    large = 1
  }
}
