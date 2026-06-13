project pkg {
  arches = ["x86_64", "aarch64", "i386"]
  rpm {
    spec = "VK_hdr_layer.spec"
  }
  labels {
        subrepo = "nvidia"
        nightly = 1
        mock = 1
    }
}
