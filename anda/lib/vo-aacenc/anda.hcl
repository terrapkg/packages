project pkg {
  arches = ["x86_64", "aarch64"]
  rpm {
    spec = "vo-aacenc.spec"
  }
  labels {
        weekly = 1
        mock = 1
    }
}
