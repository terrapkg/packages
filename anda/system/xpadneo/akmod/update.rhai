let c = sh("cat anda/system/xpadneo/kmod-common/xpadneo.spec | grep '%global commit ' | sed -E 's/.+commit //'", #{"stdout": "piped"}).ctx.stdout;
c.pop();
rpm.global("commit", c);
if rpm.changed() {
    rpm.release();
    let d = sh("cat anda/system/xpadneo/kmod-common/xpadneo.spec | grep '%global commitdate' | sed -E 's/.+commitdate //'", #{"stdout": "piped"}).ctx.stdout;
    d.pop();
    rpm.global("commitdate", d);
    let v = sh("cat anda/system/xpadneo/kmod-common/xpadneo.spec | grep '%global ver' | sed -E 's/.+ver //'", #{"stdout": "piped"}).ctx.stdout;
    v.pop();
    rpm.global("ver", v);
}

