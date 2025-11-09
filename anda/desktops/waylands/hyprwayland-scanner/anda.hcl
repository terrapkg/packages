project pkg {
	rpm {
		spec = "hyprwayland-scanner.nightly.spec"
	}
	labels {
		nightly = 1
		subrepo = "extras"
	}
}
