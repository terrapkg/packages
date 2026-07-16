project pkg {
    arches = ["x86_64"]
    rpm {
        spec = "uwsm.spec"
        update = "update.rhai"
    }
}
