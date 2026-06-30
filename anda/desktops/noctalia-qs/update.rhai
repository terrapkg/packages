import "andax/bump_extras.rhai" as bump;
import "andax/spec.rhai" as spec;

let version = find(`quickshell VERSION "([\d.]+)"`, gh_rawfile("noctalia-dev/noctalia-qs", "master", "CMakeLists.txt"), 1);

rpm.version(version);

if rpm.changed() {
  let commit = get(`https://api.github.com/repos/noctalia-dev/noctalia-qs/tags`).json_arr()[0].commit.sha;
  rpm.global("commit", commit);
}

open_file("anda/desktops/noctalia-qs/VERSION_qt6-qtbase.txt", "w").write(bump::bodhi("qt6-qtbase", bump::as_bodhi_ver(labels.branch))); // will trig rebuild when changed

let dir = sub(`/[^/]+$`, "", __script_path);
if sh("[[ `git status " + dir + " --porcelain` ]] && exit 1 || exit 0", #{}).ctx.rc == 1 {
    let rel = spec::get_release(rpm).parse_int();
    rpm.release(rel + 1);
}