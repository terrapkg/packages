import "andax/bump_extras.rhai" as bump;

fn main() {
    let branch = bump::as_bodhi_ver(labels.branch);
    let url = `https://bodhi.fedoraproject.org/updates/?search=qt6-6.&status=stable&releases=${branch}&rows_per_page=1&page=1`;
    for entry in get(url).json().updates[0].title.split(' ') {
        let matches = find_all(`qt6-([\d.]+)-(\d+)\.[\w\d]+$`, entry);
        if matches.len() != 0 {
            return matches[0][1].split(".")[1];
        }
    }
}

open_file("anda/themes/lightly-qt6/VER6.txt").write(`${main()}`); // will trig rebuild when changed
