let tags = git_tags("https://github.com/fluxerapp/fluxer");
for tag in tags {
    let v = tag;
    if v.starts_with("fluxer-app-proxy@") {
        v.crop(17);
        rpm.version(v);
        break;
    }
}
