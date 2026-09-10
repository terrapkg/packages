let v = gh("zen-browser/desktop");
rpm.global("download_ver", v);
ver.truncate(v.len - 1);
rpm.version(v);
