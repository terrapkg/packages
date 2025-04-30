project pkg {
    arches = ["x86_64"]
    rpm {
        spec = "chromebook-usbc-fix.spec"
    }
    labels {
        nightly = "1"
    }
}
