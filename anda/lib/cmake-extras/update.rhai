<<<<<<< HEAD
rpm.version(gitlab_tag("17117115"));
=======
let tags = git_tags("https://gitlab.com/ubports/development/core/cmake-extras");
rpm.version(tags[tags.len - 1]);
>>>>>>> origin/frawhide
