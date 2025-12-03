import "andax/bump_extras.rhai" as bump;

rpm.version(bump::madoguchi("zig-master", labels.branch));

if rpm.changed() {
  let r = bump::madoguchi_json("zig-master", labels.branch).rel;
  let r = sub(`(?m)(\.fc.*?|)$`, "", r).parse_int();
  rpm.release(r + 1);
}
