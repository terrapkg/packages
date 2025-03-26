project pkg {
        arches = ["x86_64"]
    rpm {
        spec = "steamtinkerlaunch-nightly.spec"
    }
    labels {
        nightly = 1
    }
}
