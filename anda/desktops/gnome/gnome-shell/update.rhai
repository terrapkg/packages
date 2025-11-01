import "andax/bump_extras.rhai" as bump;

let pkg = "gnome-shell";
let branch = bump::as_bodhi_ver(labels.branch);

let url = `https://bodhi.fedoraproject.org/updates/?search=${pkg}&status=stable&releases=${branch}&rows_per_page=10&page=1`;

let done = false;

for entry in get(url).json().updates {
  for entry in entry.title.split(' ') {
    let matches = find_all(`${pkg}-([\d.]+)-(\d+)\.[\w\d]+$`, entry);
    if matches.len() == 0 { continue; }
    let majminv = matches[0][1].split('.');
    if majminv.len() != 2 {
      print(`gnome-shell: ${matches[0][1]} has invalid version?`);
      terminate();
    }
    rpm.global("major_version", majminv[0]);
    rpm.global("minor_version", majminv[1]);
    rpm.f = sub(`Release:(\s+)(.+?)\n`, "Release:${1}" + matches[0][2] + "%{?dist}.switcheroo\n", rpm.f);
    done = true;
  }
  if done { break; }
}
