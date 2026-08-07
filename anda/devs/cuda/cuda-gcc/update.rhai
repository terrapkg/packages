import "andax/bump_extras.rhai" as bump;

let releasever = labels.branch;

if releasever.starts_with("f") {
  releasever.crop(1);
}

let gcc = "";

if releasever.starts_with("el") {
    gcc = bump::alma("gcc", "AppStream", labels.branch);
    rpm.global("gcc_major", "%{nil}");
} else if releasever >= "44" {
    gcc = bump::bodhi("gcc15", bump::as_bodhi_ver(labels.branch));
    rpm.version(gcc);
    gcc.truncate(2);
    rpm.global("gcc_major", gcc);
} else {
    gcc = bump::bodhi("gcc14", bump::as_bodhi_ver(labels.branch));
    rpm.version(gcc);
    gcc.truncate(2);
    rpm.global("gcc_major", gcc);
}
