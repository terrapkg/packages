for tag in gh_tags("ferronweb/ferron") {
    if tag.starts_with("2.") {
        rpm.version(tag);
        break;
    }
}
