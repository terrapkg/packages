project pkg {
    arches = ["x86_64"]
  rpm {
	spec = "types-colorama.spec"
  }
  labels {
    nightly = 1
  }
}
