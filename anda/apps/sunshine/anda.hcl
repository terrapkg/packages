project pkg {
  rpm {
    spec = "sunshine.spec"
    extra_repos = ["https://repos.fyralabs.com/terrarawhide-nvidia"]
  }
  labels {
        mock = 1
    }
}
