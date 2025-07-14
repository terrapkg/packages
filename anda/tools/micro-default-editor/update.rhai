let info = sh("dnf info micro -y", #{"stdout": "piped"}).ctx.stdout;
let v = find("Version\\s+: ([\\d.]+)", info, 1);
rpm.version(v);
let r = find("Release\\s+: ([\\d]+)", info, 1);
rpm.f = sub(`Release: (.+?)\n`, "Release: " + r + "%{?dist}\n", rpm.f);
let e = find("Epoch\\s+: ([\\d.]+)", info, 1);
rpm.f = sub(`Epoch: (.+?)\n`, "Epoch: " + e + "\n", rpm.f);
