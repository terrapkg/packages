project pkg {
	rpm {
		spec = "prismlauncher.spec"
        extra_repos = ["https://packages.adoptium.net/artifactory/rpm/fedora/rawhide/\\$basearch"]
	}
	labels {
		mock = 1
	}
}
