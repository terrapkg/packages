project pkg {
  arches = ["x86_64", "aarch64", "i386"]
  rpm {
    spec = "libfreeaptx.spec"
  }
  labels {
        weekly = 1
        mock = 1
    }
}
