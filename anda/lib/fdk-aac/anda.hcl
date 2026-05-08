project pkg {
         arches = ["x86_64", "aarch64", "i386"]
  rpm {
    spec = "fdk-aac.spec"
  }
  labels {
        mock=1
        weekly = 1
    }
}
