project pkg {
         arches = ["x86_64", "aarch64", "i686"]
  rpm {
    spec = "fdk-aac.spec"
  }
  labels {
        subrepo = "multimedia"
        weekly = 1
    }
}
