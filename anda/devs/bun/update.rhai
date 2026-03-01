import anda/bump_extras.rhai as bump;

rpm.version(gh_rawfile("oven-sh/bun", "main", "LATEST"));

if rpm.changed {
   rpm.global("zig_version", bump::bodhi("zig", as_bodhi_ver(labels.branch)));
}
