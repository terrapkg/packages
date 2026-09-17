project pkg {
	arches = ["x86_64", "aarch64"]
	rpm {
		spec = "cursor.spec"
		update = "update.rhai"
	}
}
