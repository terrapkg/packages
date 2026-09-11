<<<<<<< HEAD
rpm.version(gitlab_tag("25092390"));
=======
let tags = git_tags("https://gitlab.com/ubports/development/core/libusermetrics");
let f = rpm.f;
rpm.version(tags[tags.len - 1]);
>>>>>>> origin/frawhide
