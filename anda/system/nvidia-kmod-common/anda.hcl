project pkg {
    rpm {
        spec = ""
        enable_scm = true

        scm_opts = {
            method = "git"
            package = "nvidia-kmod-common"
            branch = "master"
            write_tar = "true"
            spec = "nvidia-kmod-common.spec"
            git_get = "git clone https://github.com/negativo17/nvidia-kmod-common"
        }
    }
}
