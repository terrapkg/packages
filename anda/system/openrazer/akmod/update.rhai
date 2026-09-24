let v = sh("cat anda/system/openrazer/kmod-common/openrazer.spec | grep -m1 '^Version:' | sed -E 's/^Version:\\s+//'", #{"stdout": "piped"}).ctx.stdout;
v.pop();
rpm.version(v);
