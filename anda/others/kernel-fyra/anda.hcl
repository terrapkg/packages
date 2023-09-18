project pkg {
    arches = ["x86_64", "aarch64"]
    pre_script = "pre.rhai"
    rpm {
        spec = "dummy.spec"
    }
}
