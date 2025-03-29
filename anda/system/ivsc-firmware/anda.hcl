project pkg {
    arches = ["x86_64"]
  rpm {
    spec = "ivsc-firmware.spec"
  }
  labels {
        weekly = 1
    }
}
