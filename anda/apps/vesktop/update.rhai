let v = gh_tag("Vencord/Vesktop");
let url = `dev.vencord.Vesktop.metainfo.xml`;

if get(`https://github.com/Vencord/Vesktop/releases/expanded_assets/${v}`).contains(url) {
  rpm.version(v);
} else {
  print(`vesktop: ${v} (waiting for ${url})`);
  terminate();
}

