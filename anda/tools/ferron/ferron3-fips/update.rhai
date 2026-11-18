for tag in gh_tags("ferronweb/ferron") {
    if tag.starts_with("3.") {
        rpm.global("tag", tag);
        tag.replace("-", "~");
        rpm.version(tag);
        break;
    }
}
