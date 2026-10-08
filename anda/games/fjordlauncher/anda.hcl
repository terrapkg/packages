project pkg {
	rpm {
		spec = "fjordlauncher.spec"
        extra_repos = ["https://packages.adoptium.net/artifactory/rpm/fedora/rawhide/\\$basearch"]
	}
	labels {
		mock = 1
	}
}
