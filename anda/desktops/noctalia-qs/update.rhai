import "andax/bump_extras.rhai" as bump;

fn main(labels) {
    let branch = bump::as_bodhi_ver(labels.branch);
    return bump::bodhi("qt6-6.", branch);
}

open_file("anda/desktops/noctalia-qs/VER6.txt").write(`${main(labels)}`); // will trig rebuild when changed

let release = get(`https://api.github.com/repos/noctalia-dev/noctalia-qs/tags`).json_arr()[0];

rpm.version(release.name);

if rpm.changed() {
  rpm.global("commit", release.commit.sha);
}