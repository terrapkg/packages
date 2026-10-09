// install runtime CI deps
let tools = sh("dnf5 install -y bash coreutils cpio findutils git-core make python3 rpm-build sed tar xz", #{});
if tools.ctx.rc != 0 {
    throw "Failed to install kernel-surface source preparation tools";
}

// The builder image ignores /etc/yum.repos.d and defines only binary repos, so we override it for this one time
let builddeps = sh("dnf5 --setopt=reposdir=/etc/yum.repos.d --enable-repo=fedora-source --enable-repo=updates-source builddep -y kernel", #{});
if builddeps.ctx.rc != 0 {
    throw "Failed to install Fedora kernel build dependencies";
}
