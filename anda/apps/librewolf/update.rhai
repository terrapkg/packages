let parts = codeberg_tag("librewolf/source").split("-");
rpm.version(parts[0]);
rpm.global("lw_release", parts[1]);
