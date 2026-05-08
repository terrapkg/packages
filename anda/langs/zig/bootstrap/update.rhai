let url = `https://ziglang.org/download/index.json`;
let json = get(url).json();
let v = json.master.version;
rpm.global("ver", v);

if rpm.changed() {
   rpm.release();
   // Update the Zig version in the script
   let dir = sub(`/[^/]+$`, "", __script_path);
   sh(`sed -i 's|version=.*|version=${v}|' setup.sh`, #{ "cwd": dir });
}
