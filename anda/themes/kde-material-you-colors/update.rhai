import "andax/bump_extras.rhai" as bump;
import "andax/spec.rhai" as spec;

rpm.version(pypi("kde-material-you-colors"));

open_file("anda/themes/kde-material-you-colors/VERSION_qt6-qtbase.txt", "w").write(bump::bodhi("qt6-qtbase", bump::as_bodhi_ver(labels.branch)));

let dir = sub(`/[^/]+$`, "", __script_path);
if sh("[[ `git status " + dir + " --porcelain` ]] && exit 1 || exit 0", #{}).ctx.rc == 1 {
    let rel = spec::get_release(rpm).parse_int();
    rpm.release(rel + 1);
}
