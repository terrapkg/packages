<<<<<<< HEAD
let commit = gh_commit("OpenGamingCollective/gamescope");
rpm.global("gamescope_commit", commit);
if rpm.changed() {
    rpm.release();
}
=======
let v = gh_tag("OpenGamingCollective/gamescope");

rpm.global("ver", v);
v.replace("-ogc", "^");
rpm.version(v);
>>>>>>> origin/frawhide
