let txt = get("https://discordapp.com/api/updates/canary/RELEASES");
let v = find("DiscordCanary-([\\d\\.]+)-", txt, 1);
rpm.version(v);
