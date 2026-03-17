let v = gh_tag("OpenGamingCollective/xonedo")
v.crop(1);
rpm.global("ver", v);

if rpm.changed() {
  rpm.release();
}
