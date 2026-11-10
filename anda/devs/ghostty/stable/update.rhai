let v = gh_tag("ghostty-org/ghostty");

if !v.starts_with("vt-") {
  rpm.version(v);
}
