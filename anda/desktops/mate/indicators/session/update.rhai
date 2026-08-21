let tags = git_tags("https://github.com/AyatanaIndicators/ayatana-indicator-session");
rpm.version(tags[tags.len - 1]);
