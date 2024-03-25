let o = get("https://gitlab.com/api/v4/projects/24742019/repository/tags").json_arr()[0];
rpm.version(o.name);
if rpm.changed() {
	rpm.global("commit", o.commit.id);
}
