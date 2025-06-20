project pkg {
    arches = ["x86_64"]
    rpm {
        spec = "protontricks.spec"
    }
    labels {
        subrepo = "extras"
    }
}
