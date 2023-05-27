let html = get("https://discordapp.com/api/download?platform=linux&format=tar.gz");
let newver = find("https://dl\\.discordapp\\.net/apps/linux/([\\.\\d]+)/", html, 1);
rpm.version(newver);
