let html = get("https://launchpad.net/frame");
let v = find("Latest version is v([\d.]+)", html, 1);
rpm.version(v);
