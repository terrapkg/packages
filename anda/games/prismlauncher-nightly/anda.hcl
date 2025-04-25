project pkg {
	rpm {
		spec = "prismlauncher-nightly.spec"
        extra_repos = ["https://packages.adoptium.net/artifactory/rpm/fedora/\\$releasever/\\$basearch"]
	}
	labels {
		nightly = "1"
		mock = 1
	}
}
