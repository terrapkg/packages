rpm.global("commit", gh_commit("TiPSilva/ayaneo-leds"));
if rpm.changed() {
    rpm.release();
    rpm.global("commitdate", date());
    rpm.global("ver", gh("TiPSilva/ayaneo-leds"));
}
