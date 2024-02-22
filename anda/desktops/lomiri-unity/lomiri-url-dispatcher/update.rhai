rpm.version(gitlab_tag("17424894"));
if rpm.changed() {
	rpm.global("commit", get("https://gitlab.com/api/v4/projects/17424894/repository/commits").json_arr()[0].id);
}
