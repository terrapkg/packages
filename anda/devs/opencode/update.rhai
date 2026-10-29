let tags = gh_tags("anomalyco/opencode");
tags.reverse();
for tag in tags {
    if tag.starts_with("v") && !tag.starts_with("vscode") {
        let v = tag;
        v.crop(1);
        rpm.version(v);
        break;
    }
}
