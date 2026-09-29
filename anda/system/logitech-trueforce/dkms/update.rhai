let c = sh("cat anda/system/logitech-trueforce/kmod-common/logitech-trueforce.spec | grep 'Version: ' | sed -E 's/Version: +//'", #{"stdout": "piped"}).ctx.stdout;
c.trim();
rpm.version(c);
if rpm.changed() {
    rpm.release();
}
