import "andax/bump_extras.rhai" as bump;

rpm.version(bump::madoguchi("zig-master-bootstrap", labels.branch));
if rpm.changed () {
     let v = sh("cat anda/langs/zig/bootstrap/zig-master-bootstrap.spec | grep '%global         ver' | sed -E 's/.+ver //'", #{"stdout": "piped"}).ctx.stdout;
     v.pop();
     rpm.global("ver", v);
}
