project pkg {
	rpm {
		spec = "prismlauncher.spec"
        extra_repos = ["https://packages.adoptium.net/artifactory/rpm/fedora/\\$releasever/\\$basearch"]
	}
	labels {
		mock = 1
	}
}
