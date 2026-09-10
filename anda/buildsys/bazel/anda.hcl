project pkg {
  pre_script = "pre.rhai"
  labels {
    large = 1
  }
  rpm {
    spec = "bazel.spec"
    extra_repos = ["https://packages.adoptium.net/artifactory/rpm/fedora/\\$releasever/\\$basearch"]
  }
}
