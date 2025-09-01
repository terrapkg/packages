import "andax/bump_extras.rhai" as bump;

let v = bump::bodhi_vr("neovim", bump::as_bodhi_ver(labels.branch));
let e = sh("dnf rq --qf='%{epoch}' neovim --repo=fedora,updates", #{"stdout": "piped"}).ctx.stdout;

rpm.version(v[1]);
rpm.release(v[2]);
rpm.f = sub(`^Epoch: (.+?)$`, "Epoch: " + e, rpm.f);
