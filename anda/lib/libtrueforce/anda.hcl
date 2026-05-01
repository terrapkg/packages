project pkg {
  arches = ["x86_64"]
  rpm {
    spec = "libtrueforce.spec"
  }
  labels {
        nightly = 1
        mock = 1
    }
}
