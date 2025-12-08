project pkg {
         arches = ["x86_64", "aarch64"]
  rpm {
    spec = "fdk-aac.spec"
  }
  labels {
        mock=1
        subrepo = "multimedia"
        weekly = 1
    }
}
