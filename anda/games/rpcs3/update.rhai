let release = get("https://api.github.com/repos/RPCS3/rpcs3-binaries-linux/releases/latest").json();
rpm.global("ver", release.name);

if rpm.changed () {
     let c = release.tag_name;
     c.crop(6);
     rpm.global("commit", c);
     rpm.release();
}
