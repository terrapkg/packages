project pkg {
  arches = ["x86_64", "aarch64"]
  rpm {
    spec = "gstreamer1-plugins-ugly.spec"
  }
  labels {
    subrepo = "multimedia"
    mock = 1
    updbranch = 1
  }
}
