let html = get("https://bazaar.launchpad.net/~system-settings-touch/gsettings-ubuntu-touch-schemas/trunk/changes");
let v = find("([.\\d+]+)-0ubuntu1", html, 1);
rpm.version(v);
