project pkg {
    arches = ["x86_64"]
    rpm {
        spec = "gamescope-session-opengamepadui.spec"
    }
    labels {
        nightly = 1
    }
}
