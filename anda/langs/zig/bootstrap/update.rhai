let url = `https://ziglang.org/download/index.json`;
let json = get(url).json();
let v = json.master.version;
rpm.global("ver", v);

if rpm.changed() {
   rpm.release();
   // Update the Zig version in the script
   let dir = sub(`/[^/]+$`, "", __script_path);
   sh(`sed -i 's|version=.*|version=${v}|' setup.sh`, #{ "cwd": dir });
   // Update the mirrors
   let mirrorlist = get("https://ziglang.org/download/community-mirrors.txt");
   mirrorlist.pop();
   let mirrors = sub("\n", " ", mirrorlist);
   sh(`sed -i 's|mirrorlist=.*|mirrorlist="${mirrors}"|' setup.sh`, #{ "cwd": dir });
}
