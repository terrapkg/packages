rpm.version(find(`\nVersion:\s+1:(.+?)\s`, get("https://repo.steampowered.com/steam/archive/beta/steam_latest-beta.dsc"), 1));
