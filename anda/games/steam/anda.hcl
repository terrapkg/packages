project pkg {
    arches = ["x86_64"]
	rpm {
		spec = "steam.spec"
	}
    // todo: force-arches macro?
    // labels {
    //     multilib = 1
    // }
}
