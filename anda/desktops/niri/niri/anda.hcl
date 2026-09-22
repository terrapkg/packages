project pkg {
    arches = ["x86_64"]
    rpm {
        spec = "niri.spec"
        update = "update.rhai"
    }
}
