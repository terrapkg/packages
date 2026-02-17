project pkg {
      arches = ["x86_64"]
	rpm {
      spec = "pkgcore.spec"
	}
  	labels {
      mock = 1
  }
}
