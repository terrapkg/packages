project pkg {
        arches = ["x86_64"]
    rpm {
        spec = "spotx-bash.spec"
    }
    labels {
        nightly = 1
    }
}
