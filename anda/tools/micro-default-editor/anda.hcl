project pkg {
        arches = ["x86_64"]
	rpm {
		spec = "micro-default-editor.spec"
	}
	labels {
		updbranch = 1
	}
}
