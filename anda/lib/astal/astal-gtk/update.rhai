import "andax/bump_extras.rhai" as bump;

let mg = bump::madoguchi_json("astal", labels.branch);
rpm.global("commit_date", `0\^(\d+)\.([[:xdigit:]]+)`.find(mg.ver, 1));
rpm.global("commit", `0\^(\d+)\.([[:xdigit:]]+)`.find(mg.ver, 2));
if rpm.changed() {
	rpm.release(`^(\d+)\.`.find(mg.rel, 1));
}
