let html = get("https://launchpad.net/apparmor");
let v = find("Latest version is ([\\d.]+)", html, 1);
rpm.version(v);
