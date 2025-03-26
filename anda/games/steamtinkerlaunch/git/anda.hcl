project pkg {
        arches = ["x86_64"]
    rpm {
        spec = "steamtinkerlaunch-git.spec"
    }
    labels {
        nightly = 1
    }
}
