let o = get("https://gitlab.com/api/v4/projects/17088252/repository/tags").json_arr()[0];
let f = rpm.f;
rpm.version(o.name);
// check if changed
if rpm.f != f {
	rpm.global("commit", o.commit.id);
}
