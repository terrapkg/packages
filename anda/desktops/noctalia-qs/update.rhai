import "andax/bump_extras.rhai" as bump;

fn main(labels) {
    let branch = bump::as_bodhi_ver(labels.branch);
    let url = `https://bodhi.fedoraproject.org/updates/?search=qt6-6.&status=stable&releases=${branch}&rows_per_page=1&page=1`;
    for entry in get(url).json().updates[0].title.split(' ') {
        let matches = find_all(`qt6-([\d.]+)-(\d+)\.[\w\d]+$`, entry);
        if matches.len() != 0 {
            return matches[0][1].split(".")[1];
        }
    }
}

open_file("anda/desktops/noctalia-qs/VER6.txt").write(`${main(labels)}`); // will trig rebuild when changed

let release = get(`https://api.github.com/repos/noctalia-dev/noctalia-qs/tags`).json_arr()[0];

rpm.version(release.name);

if rpm.changed() {
  rpm.global("commit", release.commit.sha);
}