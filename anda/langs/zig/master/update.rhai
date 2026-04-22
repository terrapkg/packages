import "andax/bump_extras.rhai" as bump;

rpm.version(bump::madoguchi("zig-master", labels.branch));

if rpm.changed() {
  let r = bump::madoguchi_json("zig-master", labels.branch).rel;
  let r = sub(`(?m)(\.fc.*?|)$`, "", r).parse_int();
  rpm.release(r + 1);
  // Update the needed LLVM version
  let rawfile = codeberg_rawfile("ziglang/zig", "master", "README.md");
  let l = find(`releases\.llvm\.org/download\.html#([\d.]+)`, rawfile, 1);
  rpm.global("llvm_version", l);
  l.truncate(2);
  rpm.global("llvm_compat", l);
}
