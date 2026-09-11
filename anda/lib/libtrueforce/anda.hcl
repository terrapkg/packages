project pkg {
  arches = ["x86_64"]
  rpm {
    spec = "libtrueforce.spec"
  }
  labels {
        mock = 1
    }
}
