let url = `https://ziglang.org/download/index.json`;
let json = get(url).json();
let v = json.master.version;
rpm.global("ver", v);
if rpm.changed() {
   rpm.release();
   // Update the Zig version in the script
   sh(`sed -i 's/version=.*/version=${v}/' anda/langs/zig/bootstrap/choose-mirror.sh`, #{});
   // This could be done with the rhai-rand Crate but Anda does not use this currently
   let mirror = sh("anda/langs/zig/bootstrap/choose-mirror.sh", #{"stdout": "piped"}).ctx.stdout;
   mirror.pop();
   rpm.global("mirror_url", mirror);
}
