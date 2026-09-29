let tags = git_tags("https://git.lsfg-vk.dev/lsfg-vk.git");
for tag in tags {
    let v = tag;
    if !v.contains("rc") {
        rpm.version(v);
        break;
    }
}
