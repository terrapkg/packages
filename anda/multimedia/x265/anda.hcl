project pkg {
    arches = ["x86_64", "aarch64", "i386"]
    rpm {
        spec = "x265.spec"
        extra_repos = ["https://repos.fyralabs.com/terrarawhide-multimedia"]
    }
    labels {
        mock = 1
        subrepo = "multimedia"
   }
}
