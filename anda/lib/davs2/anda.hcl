project pkg {
    arches = ["x86_64", "aarch64"]
  rpm {
    spec = "davs2.spec"
  }
  labels {
   mock = 1
   }
}
