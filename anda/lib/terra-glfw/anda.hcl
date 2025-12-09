project pkg {
  arches = ["x86_64", "aarch64", "i686"]
  rpm {
    spec = "terra-glfw.spec"
  }
  labels {
    mock = 1
  }
}
