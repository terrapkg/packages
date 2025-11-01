project pkg {
	arches = ["x86_64"]
	rpm {
		spec = "anki.spec"
	}
        labels {
                subrepo = "extras"
        }
}
