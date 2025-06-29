let v = sh("dnf info micro | grep Version | grep -Eo '[0-9]+\\.[0-9]+.*'", #{"stdout": "piped"}).ctx.stdout;
v.pop();
rpm.version(v);
let r = sh("dnf info micro | grep Release | grep -Eo '[0-9]+' | head -1", #{"stdout": "piped"}).ctx.stdout;
r.pop();
rpm.f = sub(`Release: (.+?)\n`, "Release: " + r + "%{?dist}\n", rpm.f);
let e = sh("dnf info micro | grep Epoch | grep -Eo '[0-9]+'", #{"stdout": "piped"}).ctx.stdout;
e.pop();
rpm.f = sub(`Epoch: (.+?)\n`, "Epoch: " + e + "\n", rpm.f);
