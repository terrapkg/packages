project pkg {
  arches = ["x86_64"]
  pre_script = "pre.rhai"

  rpm {
    spec = "kernel-surface.spec"
  }
  labels {
    large = 1
  }
}
