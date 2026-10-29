project pkg {
    arches = ["aarch64"]
  rpm {
    spec = "anthropic.spec"
  }
  labels {
    updbranch = 1
  }
}
