rpm.global("commit", gh_commit("OpenGamingCollective/xonedo"));
if rpm.changed() {
    rpm.release();
    rpm.global("commitdate", date());
    let v = gh("OpenGamingCollective/xonedo");
    v.crop(1);
    rpm.global("ver", v);
}
