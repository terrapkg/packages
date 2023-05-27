let html = get("https://discordapp.com/api/download/canary?platform=linux&format=tar.gz");
let newver = find("https://dl-canary\\.discordapp\\.net/apps/linux/([\\.\\d]+)/", html, 1);
rpm.version(newver);
