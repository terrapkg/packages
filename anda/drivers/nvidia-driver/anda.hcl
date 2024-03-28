project pkg {
	pre_script = "./nvidia-generate-tarballs.sh"
	rpm {
		spec = "nvidia-driver.spec"
	}
}
