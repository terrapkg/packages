let v = gh_tag("OpenGamingCollective/xonedo");

rpm.version(find(`([\d.]+)-ogc`, v, 1));