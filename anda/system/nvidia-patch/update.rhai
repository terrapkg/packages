if filters.contains("nightly") {
	rpm.global("commit", get("https://api.github.com/repos/keylase/nvidia-patch/commits/HEAD").json().sha);
	rpm.release();
}
