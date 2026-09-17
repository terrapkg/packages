project pkg {
    arches = ["aarch64"]
	rpm {
		spec = "cros-keyboard-map.spec"
	}
  labels {
    nightly = "3"
  }
}
