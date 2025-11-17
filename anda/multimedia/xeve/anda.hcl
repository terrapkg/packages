project pkg {
        arches = ["x86_64", "aarch64", "i386"]
    rpm {
        spec = "xeve.spec"
        extra_repos = ["https://repos.fyralabs.com/terra\\$releasever-multimedia"]
    }
    labels {
        mock = 1
        subrepo = "multimedia"
    }
}
