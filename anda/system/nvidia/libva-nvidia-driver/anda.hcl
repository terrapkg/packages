project "pkg" {
    rpm {
        spec = "libva-nvidia-driver.spec"
    }
    arches = ["x86_64", "aarch64"]
    labels = {
        subrepo = "nvidia"
        mock = 1
        nightly = 1
    }
}
