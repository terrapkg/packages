let v = gh_tag("Milkshiift/GoofCord");

if `[\d.]+-beta`.find_all(v).len == 0 {
  print(v);
}
