let txt = get("https://discordapp.com/api/updates/ptb/RELEASES");
let v = find("DiscordPTB-([\\d\\.]+)-", txt, 1);
rpm.version(v);
