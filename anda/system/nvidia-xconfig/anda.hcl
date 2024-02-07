project pkg {
    rpm {
        spec = ""
        enable_scm = true

        scm_opts = {
            method = "git"
            package = "terra-nvidia-xconfig"
            branch = "fedora-39"
            write_tar = "true"
            spec = "nvidia-xconfig.spec"
            git_get = "git clone https://github.com/negativo17/nvidia-xconfig"
        }
    }
}
