let tags = git_tags("git.lsfg-vk.dev/lsfg-vk/");
rpm.version(tags[tags.len()-1]);
