project "pkg" {
    rpm {
        spec = ""
        enable_scm = true

        scm_opts = {
            method = "git"
            package = "lorax"
            branch = "lorax-38.4-1"
            write_tar = "true"
            spec = "lorax.spec"
            git_get = "git clone https://github.com/weldr/lorax.git"
        }
    }
}
