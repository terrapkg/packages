let html = get("https://launchpad.net/grail");
let v = find("Latest version is ([\d.]+)", html, 1);
rpm.version(v);
