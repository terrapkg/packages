project pkg {
    rpm {
        spec = "cuda-bindings.spec"
        extra_repos = ["https://repos.fyralabs.com/terrarawhide-nvidia"]
    }
}
