let c = sh("cat anda/system/ipu6-drivers/kmod-common/intel-ipu6-drivers.spec | grep '%global ipu6_commit ' | sed -E 's/.+ipu6_commit //'", #{"stdout": "piped"}).ctx.stdout;
c.pop();
rpm.global("ipu6_commit", c);
if rpm.changed() {
    rpm.release();
    let d = sh("cat anda/system/ipu6-drivers/kmod-common/intel-ipu6-drivers.spec | grep '%global ipu6_commitdate' | sed -E 's/.+ipu6_commitdate //'", #{"stdout": "piped"}).ctx.stdout;
    d.pop();
    rpm.global("ipu6_commitdate", d);
    let v = sh("cat anda/system/ipu6-drivers/kmod-common/intel-ipu6-drivers.spec | grep '%global ver' | sed -E 's/.+ver //'", #{"stdout": "piped"}).ctx.stdout;
    v.pop();
    rpm.global("ver", v);
}

