let tag = gh_tag("OpenGamingCollective/gamescope");
rpm.version(find(`^([\d.]+)-ogc\d+$`, tag, 1));
rpm.global("ogc_release", find(`-ogc(\d+)$`, tag, 1));
