project pkg {
  rpm {
    spec = "bpf-linker-nightly.spec"
  }
  labels {
    nightly = 1
    updbranch = 1
  }
}
