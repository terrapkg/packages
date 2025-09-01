project pkg {
	rpm {
		spec = "nodejs-backport.spec"
		pre_script = "setup.sh"
	}
}
