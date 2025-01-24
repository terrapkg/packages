project pkg {
  arches = ["x86_64", "aarch64", "i386"]
  rpm {
    spec = "libde265.spec"
  }
  labels {
    mock = 1
  }
}
