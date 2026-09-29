project pkg {
	rpm {
		spec = "prismlauncher-nightly.spec"
        extra_repos = ["https://packages.adoptium.net/artifactory/rpm/fedora/rawhide/\\$basearch"]
	}
	labels {
		nightly = 4
		mock = 1
	}
}
