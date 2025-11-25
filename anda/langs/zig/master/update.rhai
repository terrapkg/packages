import "andax/bump_extras.rhai" as bump;

rpm.version(bump::madoguchi("zig-master", labels.branch));

if rpm.changed {
  let dir = sub(`/[^/]+$`, "", __script_path);
  let r = bump::madoguchi_json("gstreamer1-plugins-bad", labels.branch).rel;
  rpm.release(r + 1);
}

