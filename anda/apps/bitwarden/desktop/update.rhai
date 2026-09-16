let v = gh("bitwarden/client");
if v.starts_with("desktop-v") {
    v.crop(9);
    rpm.version(v);
}
