let v = gh("stakira/OpenUtau");
let url = `OpenUtau-linux-x64.tar.gz`

if get(`https://github.com/stakira/OpenUtau/releases/expanded_assets/${v}`).contains(url) {
  rpm.global("ver", v);
} else {
  print(`openutau: ${v} (waiting for bundle)`);
  terminate();
}
