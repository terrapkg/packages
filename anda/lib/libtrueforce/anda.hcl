project pkg {
  arches = ["x86_64"]
  rpm {
    spec = "libtrueforce.spec"
  }
  labels {
        updbranch = 1
        mock = 1
    }
}
