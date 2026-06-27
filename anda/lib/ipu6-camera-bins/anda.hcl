project pkg {
   arches = ["x86_64"]
  rpm {
    spec = "ipu6-camera-bins.spec"
  }
  labels {
        nightly = 1
    }
}
