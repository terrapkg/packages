project pkg {
    arches = ["x86_64"]
    rpm {
        spec = "waydroid-nvidia.spec"
    }
    labels {
        subrepo = "extras"
    }
}