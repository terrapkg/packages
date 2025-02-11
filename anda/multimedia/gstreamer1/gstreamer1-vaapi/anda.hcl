project pkg {
  arches = ["x86_64", "aarch64", "i386"]
  rpm {
    spec = "gstreamer1-vaapi.spec"
  }
  labels {
        extra = 1
        mock = 1
    }
}
