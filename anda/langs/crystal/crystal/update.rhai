let html = get("https://crystal-lang.org/");
rpm.version(find("Latest release: <strong>(.+?)</strong>", html, 1))
