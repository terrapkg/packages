let v = gh("crystal-lang/crystal");
let url = `crystal-${v}-1-linux-x86_64-bundled.tar.gz`;

if get(`https://github.com/crystal-lang/crystal/releases/expanded_assets/${v}`).contains(url) {
  rpm.version(v);
} else {
  print(`crystal: ${v} (waiting for bundle)`);
  terminate();
}
