let ver = gh_tag("apache/groovy");
ver.replace("GROOVY_", "");
ver.replace("_", ".");
rpm.version(ver);
