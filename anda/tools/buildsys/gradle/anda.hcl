project pkg {
    arches = ["x86_64"]
	rpm {
		spec = "gradle.spec"
    extra_repos = ["https://packages.adoptium.net/artifactory/rpm/fedora/\\$releasever/\\$basearch"]
	}
}
