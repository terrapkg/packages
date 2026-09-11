let v = gh_tag("linuxmint/sticky");
if v.starts_with("1") {
    rpm.version(v);
}
