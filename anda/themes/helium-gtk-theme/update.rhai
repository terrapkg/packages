rpm.global("ver", gh("tau-OS/tau-helium"));

if rpm.changed() {
    rpm.release();
}
