rpm.version(gitlab_tag("19057685"));
if rpm.changed() {
	rpm.global("commit", gitlab_commit("19057685", "main"));
}
