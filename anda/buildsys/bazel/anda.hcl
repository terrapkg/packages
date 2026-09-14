project pkg {
  pre_script = "pre.rhai"
  rpm {
    spec = "bazel.spec"
    extra_repos = ["https://packages.adoptium.net/artifactory/rpm/fedora/rawhide/\\$basearch"]
  }
}
