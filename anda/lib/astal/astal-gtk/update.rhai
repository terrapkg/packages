import "andax/bump_extras.rhai" as bump;
import "andax/spec.rhai" as spec;

let mg = bump::madoguchi_json("astal", labels.branch);
rpm.global("commit_date", `0\^(\d+)\.([[:xdigit:]]+)`.find(mg.ver, 1));
rpm.global("shortcommit", `0\^(\d+)\.([[:xdigit:]]+)`.find(mg.ver, 2));
if rpm.changed() {
	rpm.release(`^(\d+)\.`.find(mg.rel, 1));
	rpm.global("commit", spec::get_global(#{
		f: open_file("anda/lib/astal/astal/astal.spec").read_string()
	}, "commit"));
}
