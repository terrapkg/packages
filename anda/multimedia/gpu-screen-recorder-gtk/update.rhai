let tags = git_tags("https://repo.dec05eba.com/gpu-screen-recorder-gtk");
rpm.version(tags[tags.len()-1]);
