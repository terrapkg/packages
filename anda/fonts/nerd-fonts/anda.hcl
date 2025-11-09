project pkg {
	arches = ["x86_64"]
	rpm {
		spec = "nerd-fonts.spec"
	}
	labels {
		no_upload_srpms = 1
	}
}
