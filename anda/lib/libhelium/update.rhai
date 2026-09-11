rpm.global("ver",gh("tau-OS/libhelium"));
if rpm.changed() {
	rpm.release();
}
