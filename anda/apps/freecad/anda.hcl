project pkg {
    arches = ["x86_64", "aarch64"]
    rpm {
        spec = "freecad.spec"
    }
    labels = {
        large = 1
    }
}
