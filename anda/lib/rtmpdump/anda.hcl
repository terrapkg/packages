project pkg {
    arches = ["x86_64", "aarch64"]
  rpm {
    spec = "rtmpdump.spec"
  }
  labels {
    mock = 1
    subrepo = "multimedia"
  }
}
