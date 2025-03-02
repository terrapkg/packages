let c = sh("cat anda/system/xone/kmod-common/xone-kmod-common.spec | grep '%global commit' | sed -E 's/.+commit //'", #{"stdout": "piped"}).ctx.stdout;
c.pop();
rpm.global("commit", c);
if rpm.changed() {
    rpm.release();
    let d = sh("cat anda/system/xone/kmod-common/xone-kmod-common.spec | grep '%global date' | sed -E 's/.+date //'", #{"stdout": "piped"}).ctx.stdout;
    d.pop();
    rpm.global("date", d);
    let v = sh("cat anda/system/xone/kmod-common/xone-kmod-common.spec | grep '%global ver' | sed -E 's/.+ver //'", #{"stdout": "piped"}).ctx.stdout;
    v.pop();
    rpm.global("ver", v);
}

