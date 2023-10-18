let html = get("https://download.kde.org/stable/liquidshell/");
rpm.version(find(`>liquidshell-([.\d]+)\.tar\.xz</a>`, html, 1));
