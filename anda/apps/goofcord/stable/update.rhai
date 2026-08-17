let v = gh_tag("Milkshiift/GoofCord");

if `[\d.]+-beta\.\d+`.find_all(v).len == 0 {
  rpm.version(v);
}
