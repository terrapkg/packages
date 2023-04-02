let html = get("https://launchpad.net/geis");
let v = find("Latest version is ([\\d.]+)", html, 1);
rpm.version(v);
