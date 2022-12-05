let html = get("https://discordapp.com/api/download/ptb?platform=linux&format=tar.gz");
let newver = str(find("https://dl-ptb\.discordapp\.net/apps/linux/([\.\d]+)/", html, 1) @ 0);
rpm.version(newver);