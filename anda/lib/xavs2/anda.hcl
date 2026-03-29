project pkg {
    arches = ["x86_64", "aarch64", "i386"]
  rpm {
    spec = "xavs2.spec"
  }
  labels {
    mock = 1
    weekly = 1
  }
}
