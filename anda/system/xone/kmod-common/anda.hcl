project pkg {
               arches = ["x86_64"]
	rpm {
		spec = "xone-kmod-common.spec"
		pre_script = "fetch-tou.sh"
	}
	labels {
		mock = 1
                nightly = 1
	}
}
