import "andax/bump_extras.rhai" as bump;

open_file("anda/terra/gpg-keys/RELEASE.txt", "w").write(bump::as_bodhi_ver(labels.branch));

let dir = sub(`/[^/]+$`, "", __script_path);
if sh("[[ `git status " + dir + " --porcelain` ]] && exit 1 || exit 0", #{}).ctx.rc == 1 {
    rpm.release();
}
