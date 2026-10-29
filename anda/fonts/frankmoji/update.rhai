let html = get("https://frankmoji.com/");
rpm.global("fonttag", find("FrankMoji(\\w+)-Font\\.zip", html, 1));
rpm.version(find("<dt>Version</dt>\\s*<dd>([\\d.]+)</dd>", html, 1));
