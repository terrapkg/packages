project pkg {
   arches = ["x86_64"]
  rpm {
    spec = "ipu6-camera-hal.spec"
  }
  labels {
        nightly = 1
    }
}
