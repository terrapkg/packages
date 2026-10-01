project pkg {
        arches = ["aarch64"]
    rpm {
        spec = "git-dude.spec"
    }
    labels {
        nightly = 3
    }
}
