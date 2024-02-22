rpm.version(gitlab_tag("25716028"));
if rpm.changed() {
	rpm.global("commit", get("https://gitlab.com/api/v4/projects/25716028/repository/commits").json_arr()[0].id);
}
