let tags = git_tags("https://gitlab.com/ubports/development/core/lomiri-api");
let ver = tags[tags.len - 1];
rpm.version(ver);
