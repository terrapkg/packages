project pkg {
  arches = ["x86_64", "aarch64", "i386"]
  rpm {
    spec = "gstreamer1-vaapi.spec"
    extra_repos = ["https://repos.fyralabs.com/terrarawhide-multimedia"]
  }
  labels {
        subrepo = "multimedia"
        mock = 1
        updbranch = 1
    }
}
