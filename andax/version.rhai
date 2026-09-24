/// Update nightly package globals when the commit changes.
fn version_nightly(rpm, stable_ver, commit_hash) {
    commit_hash.trim();
    if rpm.global_value("commit") == commit_hash {
        return;
    }

    rpm.global("commit", commit_hash);
    rpm.global("commitdate", date());
    stable_version(rpm, stable_ver);
}

/// Update the stable version global for a nightly or quaterdaily package.
fn stable_version(rpm, stable_ver) {
    stable_ver = stable_ver.trim();
    if stable_ver.starts_with("v") {
        stable_ver.crop(1);
    }
    stable_ver = stable_ver.replace("-", ".");
    rpm.global("ver", stable_ver);
    if rpm.changed() {
        rpm.release();
    }
}

/// Fetch and update nightly package globals, querying the stable version only when the commit changes.
fn gh_nightly(rpm, repo) {
    let commit = gh_commit(repo);
    if rpm.global_value("commit") == commit.trim() {
        return;
    }
    version_nightly(rpm, gh(repo), commit);
}

/// Update quaterdaily package globals when the commit changes.
fn version_quaterdaily(rpm, stable_ver, commit_hash) {
    commit_hash.trim();
    if rpm.global_value("commit") == commit_hash {
        return;
    }

    rpm.global("commit", commit_hash);
    rpm.global("commitdate", date());
    rpm.global("run", quaterdaily_run().to_string());
    stable_version(rpm, stable_ver);
}


/// Fetch and update quaterdaily package globals, querying the stable version only when the commit changes.
fn gh_quaterdaily(rpm, repo) {
    let commit = gh_commit(repo);
    if rpm.global_value("commit") == commit.trim() {
        return;
    }
    version_quaterdaily(rpm, gh(repo), commit);
}
