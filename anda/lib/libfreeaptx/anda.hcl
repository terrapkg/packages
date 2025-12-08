project pkg {
  arches = ["x86_64", "aarch64"]
  rpm {
    spec = "libfreeaptx.spec"
  }
  labels {
        weekly = 1
        mock = 1
        subrepo = "multimedia"
    }
}
