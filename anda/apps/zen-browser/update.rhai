let v = gh("zen-browser/desktop");
ver.truncate(v.len - 1);
rpm.version(v);

rpm.global("download_ver", ("zen-browser/desktop"));
