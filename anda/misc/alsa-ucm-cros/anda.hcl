project pkg {
    arches = ["x86_64"]
  rpm {
	  spec = "alsa-ucm-cros.spec"
  }
  labels {
    updbranch = 1
    subrepo = "extras"
  }
}
