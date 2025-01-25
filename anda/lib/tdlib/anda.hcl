project pkg {
	rpm {
		spec = "tdlib-nightly.spec"
	}
	labels {
		nightly = "1"
                mock = 1
	}
}
