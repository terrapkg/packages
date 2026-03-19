if rpm.changed() {
    rpm.release();
    let v = gh_tag("OpenGamingCollective/gamescope"));
    v.crop(1);
    rpm.global("gamescope_commit", v);
}
