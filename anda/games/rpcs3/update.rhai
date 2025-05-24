let html = get("https://rpcs3.net/download");
let v = find("Build ([\\d.]+-[\\d.]+)\\s+</span>", html, 1);
rpm.global("ver", v);

if rpm.changed () {
     let c = find("Commit <a href=\"https://github.com/RPCS3/rpcs3/commit/([\\w\\d]+)\" target=\"_blank\"", html, 1);
     rpm.global("commit", c);
}
