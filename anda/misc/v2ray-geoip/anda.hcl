project pkg {
  arches = ["x86_64"]
  rpm {
    spec = "v2ray-geoip.spec"
  }
  labels {
    nightly = 1
  }
}
