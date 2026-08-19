let tags = git_tags("https://repo.dec05eba.com/gpu-screen-recorder-ui");
rpm.version(tags[tags.len()-1]);
