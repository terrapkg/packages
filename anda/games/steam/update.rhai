rpm.version(find(`\nVersion:\s+1:(.+?)\s`, get("https://repo.steampowered.com/steam/archive/stable/steam_latest.dsc"), 1));
