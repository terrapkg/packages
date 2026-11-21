let c = sh("cat anda/system/hid-hori/kmod-common/hid-hori.spec | grep 'Version: ' | sed -E 's/Version: +//'", #{"stdout": "piped"}).ctx.stdout;
c.trim();
rpm.version(c);
if rpm.changed() {
    rpm.release();
}
