let version = git_tag("https://github.com/xarbit/plasma6-applet-appgrid")
    .trim_start_matches("v");

set_version(version);
