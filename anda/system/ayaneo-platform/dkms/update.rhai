let c = sh("cat anda/system/ayaneo-platform/kmod-common/ayaneo-platform.spec | grep 'Version: ' | sed -E 's/Version: +//'", #{"stdout": "piped"}).ctx.stdout;
c.trim();
rpm.version(c);
if rpm.changed() {
    rpm.release();
}
