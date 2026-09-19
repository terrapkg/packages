project pkg {
  arches = ["x86_64"]
  pre_script = "pre.rhai"

  rpm {
    spec = "surface-kernel.spec"
  }
  labels {
    large = 1
  }
}
