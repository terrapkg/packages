project pkg {
        arches = ["x86_64"]
    rpm {
        spec = "curl_cffi.spec"
    }
   	labels {
      nightly = 1
	}
}
