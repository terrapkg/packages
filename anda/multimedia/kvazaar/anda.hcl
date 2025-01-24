project pkg {
        arches = ["x86_64", "aarch64", "i386"]
    rpm {
        spec = "kvazaar.spec"
    }
    labels {
       mock =1
    }
}
