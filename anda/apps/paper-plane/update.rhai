let ver = gh_tag("paper-plane-developers/paper-plane");
ver.crop(1);
rpm.global("ver", ver);
ver.replace("-", "~");
rpm.version(ver);
