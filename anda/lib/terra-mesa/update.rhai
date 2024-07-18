let v = gitlab_tag("gitlab.freedesktop.org", "176");
v.crop(5);
rpm.global("ver", v);
