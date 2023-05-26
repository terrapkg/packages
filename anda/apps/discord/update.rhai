let txt = get("https://discordapp.com/api/updates/RELEASES");
let v = find("Discord-([\\d\\.]+)-", txt, 1);
rpm.version(v);
