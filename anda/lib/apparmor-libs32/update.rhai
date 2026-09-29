let v = gitlab_tag("4484878");
rpm.global("normver", v);
v.replace("-", "~");
rpm.version(v);
