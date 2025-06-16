let c = sh("cat anda/system/usbio-drivers/kmod-common/intel-usbio-drivers.spec | grep '%global commit ' | sed -E 's/.+commit //'", #{"stdout": "piped"}).ctx.stdout;
c.pop();
rpm.global("commit", c);
if rpm.changed() {
    rpm.release();
    let d = sh("cat anda/system/usbio-drivers/kmod-common/intel-usbio-drivers.spec | grep '%global commit_date' | sed -E 's/.+commit_date //'", #{"stdout": "piped"}).ctx.stdout;
    d.pop();
    rpm.global("commit_date", d);
}

