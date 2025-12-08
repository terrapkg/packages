project pkg {
    arches = ["x86_64", "aarch64"]
    rpm {
        spec = "ffmpeg.spec"
        extra_repos = ["https://repos.fyralabs.com/terra\\$releasever-nvidia"]
    }
    labels {
        updbranch = 1
        mock = 1
        subrepo = "extras"
    }
}
