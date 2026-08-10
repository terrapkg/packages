let v = gh_tag("pingdotgg/t3code");
v.crop(1);
rpm.global("ver", v);
v.replace("-", "~");
rpm.version(v);
