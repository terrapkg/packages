project pkg {
  arches = ["x86_64", "aarch64", "i686"]
  rpm {
    spec = "terra-glfw.spec"
  }
  labels {
    extras = 1
    mock = 1
  }
}
