import "andax/bump_extras.rhai" as bump;
import "andax/spec.rhai" as spec;

let branch = bump::as_bodhi_ver(labels.branch);

if branch.starts_with("F") {
  branch.crop(1);
  let releasever = branch;
} else if branch.starts_with("EPEL") {
  let releasever = labels.branch;
  releasever.crop(2);
}

rpm.version(releasever);

sh(`anda/terra/gpg-keys/update-gpg-keys.sh`, #{});
let dir = sub(`/[^/]+$`, "", __script_path);
if sh("[[ `git status " + dir + " --porcelain` ]] && exit 1 || exit 0", #{}).ctx.rc == 1 {
    let rel = spec::get_release(rpm).parse_int();
    rpm.release(rel + 1);
}
