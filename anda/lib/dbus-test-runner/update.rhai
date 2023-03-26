let html = get("https://launchpad.net/dbus-test-runner");
let v = find("Latest version is ([\\d.]+)", html, 1);
rpm.version(v);
