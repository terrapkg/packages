project pkg {
    arches = ["x86_64", "aarch64"]
  rpm {
    spec = "xavs.spec"
  }
  labels {
    mock = 1
  }
}
