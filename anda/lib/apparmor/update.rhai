let html = get("https://launchpad.net/apparmor");
let v = find("Latest version is ([\\d.\\w\\-]+)", html, 1);
v.replace('-', '~');
rpm.version(v);
