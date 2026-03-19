if rpm.changed() {
    rpm.release();
    let v = gh_commit("OpenGamingCollective/gamescope"));
    v.crop(1);
    rpm.global("gamescope_commit", v);
}
