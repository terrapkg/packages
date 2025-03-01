project "pkg" {
    rpm {
        spec = "nvidia-driver.spec"
        # We run the negativo17 generator script here because I genuinely tried fixing the spec file with our fancy patch and it didn't work
        # TODO: Port it inside the specfile scripts
        # pre_script = "nvidia-generate-tarballs.sh"
    }
    arches = ["x86_64", "aarch64", "i386"]
    labels = {
        subrepo = "nvidia"
        mock = 1
    }
}