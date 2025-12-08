project pkg {
    arches = ["x86_64", "aarch64"]
        rpm {
		spec = "mesa-compat.spec"
	}
    labels {
        mock = 1
        subrepo = "mesa"
    }
}
