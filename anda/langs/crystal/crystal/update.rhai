let v = gh("crystal-lang/crystal");
let url = `https://github.com/crystal-lang/crystal/releases/download/${v}/crystal-${v}-1-linux-x86_64-bundled.tar.gz`;
try {
  find(url, get(`https://github.com/crystal-lang/crystal/releases/tag/${v}`), 0);
  rpm.version(v);
} catch {
  print(`crystal: ${v} (waiting for bundle)`);
  terminate();
}
