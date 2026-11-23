project pkg {
        arches = ["x86_64", "aarch64"]
    labels {
        large = 1
    }
    rpm {
        spec = "waterfox.spec"
    }
}
