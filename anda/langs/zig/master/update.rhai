import "andax/bump_extras.rhai" as bump;

rpm.version(bump::madoguchi("zig-master-bootstrap", labels.branch));
if rpm.changed() {
   // This could be done with the rhai-rand Crate but Anda does not use this currently
   let mirror = sh("anda/langs/zig/bootstrap/choose-mirror.sh", #{"stdout": "piped"}).ctx.stdout;
   mirror.pop();
   rpm.global("mirror_url", mirror);
}
