let v = "1.22.5-beta.1";
let v = sub(`-beta\.\d+`, "", v);
print(v);
