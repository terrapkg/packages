// Source generation runs before the generated spec's BuildRequires are resolved.
let tools = sh("dnf5 --refresh install -y bash coreutils cpio curl findutils git-core make gcc bison flex python3 rpm-build sed tar xz", #{});
if tools.ctx.rc != 0 {
    throw "Failed to install kernel-surface source preparation tools";
}

// The builder image ignores the standard source-repo definitions by default.
let builddeps = sh("dnf5 --refresh --setopt=reposdir=/etc/yum.repos.d --enable-repo=fedora-source --enable-repo=updates-source builddep -y kernel", #{});
if builddeps.ctx.rc != 0 {
    throw "Failed to install Fedora kernel build dependencies";
}
