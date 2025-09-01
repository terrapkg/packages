let v = gitlab("71087662");
if v.starts_with("Prod-Beta-") {
  v.crop(10);
  rpm.version(v);
} else {
  print(`zoi: found release: ${v}`);
}
