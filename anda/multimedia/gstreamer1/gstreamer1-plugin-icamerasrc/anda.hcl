project pkg {
  arches = ["x86_64"]
  rpm {
    spec = "gstreamer1-plugin-icamerasrc.spec"
  }
  labels {
        weekly = 1
    }
}
