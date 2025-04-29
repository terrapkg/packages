project pkg {
   arches = ["x86_64"]
    rpm {
        spec = "cuda-sandbox.spec"
    }
    labels {
	    subrepo = "nvidia"
	    updbranch = 1
    }
}
