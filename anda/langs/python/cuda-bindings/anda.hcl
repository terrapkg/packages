project pkg {
    rpm {
        spec = "cuda-bindings.spec"
        extra_repos = ["https://repos.fyralabs.com/terra\\$releasever-nvidia"]
    }
}
