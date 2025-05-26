rpm.global("commit", gh_commit("medusalix/xpad-noone"));
if rpm.changed() {
    rpm.release();
    rpm.global("commitdate", date());
    let html = get(`https://raw.githubusercontent.com/medusalix/xpad-noone/refs/heads/master/dkms.conf`);
    let v = find("PACKAGE_VERSION=\"([\\d.]+)\"", html, 1);
    rpm.global("ver", v);
}
