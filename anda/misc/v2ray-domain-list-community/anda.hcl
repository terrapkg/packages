project pkg {
  arches = ["x86_64"]
  rpm {
    spec = "v2ray-domain-list-community.spec"
  }
  labels {
    nightly = 1
  }
}
