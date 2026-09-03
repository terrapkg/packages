project pkg {
  arches = ["aarch64"]
  rpm {
    spec = "nohang-nightly.spec"
  }
  labels {
    nightly = 1
  }
}
