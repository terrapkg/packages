project pkg {
        arches = ["x86_64"]
	rpm {
		spec = "dkms-mediatek-mt7927.spec"
	}
	labels {
		updbranch = 1
		mock = 1
	}
}
