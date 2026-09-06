project pkg {
    arches = ["x86_64"]
    rpm {
        spec = "gamescope-session-ogui-steam.spec"
    }
    labels {
        nightly = 1
    }
}
