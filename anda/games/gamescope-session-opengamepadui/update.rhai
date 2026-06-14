rpm.global("commit", gh_commit("OpenGamingCollective/gamescope-session-opengamepadui"));    
if rpm.changed() {
        rpm.release();
        rpm.global("commit_date", date());
}
