project pkg {
    arches = ["x86_64"]
	rpm {
		spec = "glasgow.spec"
	}
 labels {
    nightly = 1
  }
}
