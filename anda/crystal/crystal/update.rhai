let html = get("https://crystal-lang.org/");
rpm.version(find("Latest release <.+>(.+)<\\/a>", html, 1))
