let common = sh("cat anda/system/nct6687d/kmod-common/nct6687d.spec", #{"stdout": "piped"}).ctx.stdout;
rpm.global("commit", find(`(?m)^%global commit\s+(\S+)`, common, 1));
rpm.global("commitdate", find(`(?m)^%global commitdate\s+(\S+)`, common, 1));
rpm.version(find(`(?m)^Version:\s*(\S+)`, common, 1));
rpm.release(find(`(?m)^Release:\s*(\d+)`, common, 1).parse_int());
