import "andax/bump_extras.rhai" as bump;

rpm.version(bump::madoguchi("zig-master-bootstrap", labels.branch));

if rpm.changed {
   let mirrorlist = get("https://ziglang.org/download/community-mirrors.txt");
   mirrorlist.pop();
   let mirrors = sub("\n", " ", mirrorlist);
   rpm.global("zig_mirrors", mirrors);
}
