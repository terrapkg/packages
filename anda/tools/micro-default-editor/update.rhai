let v = sh("dnf rq --qf='%{version}|%{release}|%{epoch}' micro --repo=fedora,updates", #{"stdout": "piped"}).ctx.stdout;
let vre = v.split("|");
rpm.version(vre[0]);
rpm.release(vre[1].split(".")[0].parse_int());
rpm.f = sub(`^Epoch: (.+?)$`, "Epoch: " + vre[2], rpm.f);
