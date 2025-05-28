project pkg {
        arches = ["x86_64"]
    rpm {
        spec = "rtl8821cu-kmod-common.spec"
    }
   	labels {
		nightly = "1"
	}
}
