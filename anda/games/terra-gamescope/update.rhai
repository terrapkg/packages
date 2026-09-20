let v = gh_tag("OpenGamingCollective/gamescope");

rpm.global("ver", v);
v.replace("-ogc", "^");
rpm.version(v);
