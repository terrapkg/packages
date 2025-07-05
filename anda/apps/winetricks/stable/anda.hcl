project pkg {
    arches = ["x86_64"]
    rpm {
        spec = "winetricks.spec"
    }
    labels {
        subrepo = "extras"
    }
}
