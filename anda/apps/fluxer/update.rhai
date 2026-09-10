let tags = gh_tags("fluxerapp/fluxer");
for tag in tags {
    let v = tag;
    if v.starts_with("fluxer-desktop-canary@") {
        v.crop(22);
        rpm.version(v);
        break;
    }
}
