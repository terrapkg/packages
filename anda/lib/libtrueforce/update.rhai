 let c = sh("cat anda/system/logitech-rs50-linux-driver/kmod-common/logitech-rs50-linux-driver.spec | grep '%global commit ' | sed -E 's/.+commit //'", #{"stdout": "piped"}).ctx.stdout;
c.pop();
rpm.global("commit", c);
if rpm.changed() {
    rpm.release();
    let d = sh("cat anda/system/logitech-rs50-linux-driver/kmod-common/logitech-rs50-linux-driver.spec | grep '%global commitdate' | sed -E 's/.+commitdate //'", #{"stdout": "piped"}).ctx.stdout;
    d.pop();
    rpm.global("commitdate", d);
}
