import "andax/bump_extras.rhai" as bump;

let v = bump::alma_vr("kernel", labels.branch)[1];
let r = bump::alma_vr("kernel", labels.branch)[2];
print(v);
print(r);
