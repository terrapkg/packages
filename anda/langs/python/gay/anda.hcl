project pkg {
        arches = ["x86_64"]
    rpm {
        spec = "gay.spec"
    }
   	labels {
      nightly = 1
	}
}
