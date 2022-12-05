project "pkg" {
    rpm {
        spec = "youki.spec"
        update = ""

        // enable_scm = true

        // scm_opts = {
        //     method = "git"
        //     git_get = "git clone --recursive https://github.com/containers/youki.git"
        //     write_tar = "True"
        //     package = "youki"
        // }
    }
}
