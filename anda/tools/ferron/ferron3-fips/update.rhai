let v = gh("ferronweb/ferron");
if v.starts_with("3") {
    rpm.global("tag", v);
    v.replace("-", "~");
    rpm.version(v);
}
