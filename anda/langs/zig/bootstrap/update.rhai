let url = `https://ziglang.org/download/index.json`;
let json = get(url).json();
let v = json.master.version;
rpm.global("ver", v);

if rpm.changed() {
   rpm.release();
   let mirrorlist = get("https://ziglang.org/download/community-mirrors.txt");
   mirrorlist.pop();
   let mirrors = sub("\n", " ", mirrorlist);
   rpm.global("zig_mirrors", mirrors);
}
