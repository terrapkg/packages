project pkg {
        arches = ["x86_64", "aarch64"]
    rpm {
        spec = "kvazaar.spec"
    }
    labels {
       mock = 1
    }
}
