project pkg {
   arches = ["x86_64", "aarch64"]
    rpm {
        spec = "cuda-sanitizer.spec"
    }
    labels {
        mock = 1
        subrepo = "nvidia"
        updbranch = 1
    }
}
