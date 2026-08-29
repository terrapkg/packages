let tags = git_tags("https://repo.dec05eba.com/gpu-screen-recorder-notification");
rpm.version(tags[tags.len()-1]);
