let commit = gh_commit("OpenGamingCollective/gamescope");
rpm.global("gamescope_commit", commit);
if rpm.changed() {
    rpm.release();
}
