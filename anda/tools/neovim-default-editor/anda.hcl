project pkg {
        arches = ["x86_64"]
	rpm {
		spec = "neovim-default-editor.spec"
	}
	labels {
		updbranch = 1
	}
}
