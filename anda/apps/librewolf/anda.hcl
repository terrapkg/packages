project pkg {
      arches = ["x86_64", "aarch64"]
    labels {
        large = 1
        oglyad_ignore = "drift"
    }
    rpm {
        spec = "librewolf.spec"
    }
}
