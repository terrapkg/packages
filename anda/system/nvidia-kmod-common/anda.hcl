project pkg {
    rpm {
        spec = ""
        enable_scm = true

        scm_opts = {
            method = "git"
            package = "nvidia-kmod-common"
            branch = "fedora-39"
            write_tar = "true"
            spec = "nvidia-kmod-common.spec"
            git_get = "git clone https://github.com/negativo17/nvidia-kmod-common"
        }
    }
}
