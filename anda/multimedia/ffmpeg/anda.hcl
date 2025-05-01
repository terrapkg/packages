project pkg {
    arches = ["x86_64", "aarch64", "i386"]
    extra_repos = ["https://repos.fyralabs.com/terra\\$releasever-nvidia"]
    rpm {
        spec = "ffmpeg.spec"
    }
    labels {
        updbranch = 1
        mock = 1
    }
}
