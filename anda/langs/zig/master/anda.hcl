project pkg {
	rpm {
		spec = "zig-master.spec"
	}
	labels {
		oglyad_ignore = "duplicate-name"
		updbranch = 1
		large = 1
	}
}
