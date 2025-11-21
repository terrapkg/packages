let v = gh("bitwarden/clients");
if v.starts_with("cli-v") {
    v.crop(5);
    rpm.version(v);
}
