let url = `https://ziglang.org/download/index.json`;
let json = get(url).json();
let v = json.master.version;
rpm.global("ver", v);
if rpm.changed() {
   rpm.release();
}
