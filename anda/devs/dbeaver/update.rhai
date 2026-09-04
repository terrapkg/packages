let v = gh("dbeaver/dbeaver");
let url1 = `dbeaver-ce-${v}-linux-x86_64.tar.gz`;
let url2 = `dbeaver-ce-${v}-linux-aarch64.tar.gz`;
let html = get(`https://github.com/dbeaver/dbeaver/releases/expanded_assets/${v}`);

if html.contains(url1) && html.contains(url2) {
  rpm.version(v);
} else {
  print(`dbeaver: ${v} (waiting for bundle)`);
  terminate();
}
