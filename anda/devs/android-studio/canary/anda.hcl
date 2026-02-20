project pkg {
  arches = ["x86_64"]
  rpm {
    spec = "android-studio-canary.spec"
  }
  labels { 
    nightly = "1" 
  }
}
