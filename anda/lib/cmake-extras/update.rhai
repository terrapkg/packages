let tags = git_tags("https://gitlab.com/ubports/development/core/cmake-extras");
rpm.version(tags[tags.len - 1]);
