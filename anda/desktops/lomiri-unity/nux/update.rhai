let v = find(`Latest version is ([\d.]+)`, get("https://launchpad.net/nux"), 1);
rpm.version(v);
