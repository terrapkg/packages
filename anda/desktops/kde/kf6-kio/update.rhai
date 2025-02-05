import "andax/bump_extras.rhai" as bump;

let pkg = "kf6-kio";
let branch = bump::as_bodhi_ver(labels.branch);

let url = `https://bodhi.fedoraproject.org/updates/?search=${pkg}&status=stable&releases=${branch}&rows_per_page=1&page=1`;

for entry in get(url).json().updates[0].title.split(' ') {
  let matches = find_all(`${pkg}-([\d.]+)-(\d+)\.[\w\d]+$`, entry);
  if matches.len() == 0 { continue; }
  if matches[0][1].ends_with(".0") {
    rpm.global("majmin_ver_kf6", matches[0][1][0..matches[0][1].len()-2]);
    rpm.f = sub(`Release: (.+?)\n`, "Release: " + matches[0][2] + "%{?dist}.switcheroo\n", rpm.f);
  }
  break;
}
