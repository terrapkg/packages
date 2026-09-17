 let c = sh("cat anda/system/nct6687d/kmod-common/nct6687d.spec | grep '%global commit ' | sed -E 's/.+commit //'", #{"stdout": "piped"}).ctx.stdout;
c.pop();
rpm.global("commit", c);
if rpm.changed() {
    rpm.release();
    let d = sh("cat anda/system/nct6687d/kmod-common/nct6687d.spec | grep '%global commitdate' | sed -E 's/.+commitdate //'", #{"stdout": "piped"}).ctx.stdout;
    d.pop();
    rpm.global("commitdate", d);
}
