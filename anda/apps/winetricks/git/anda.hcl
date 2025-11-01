project pkg {
    arches = ["x86_64"]
    rpm {
        spec = "winetricks-git.spec"
    }
    labels {
        subrepo = "extras"
        nightly = 1
    }
}
