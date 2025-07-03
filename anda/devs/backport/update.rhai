let json = get("https://registry.npmjs.org/backport").json();
rpm.version(json["dist-tags"]["latest"]);
