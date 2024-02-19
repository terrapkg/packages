let md = get("https://raw.githubusercontent.com/OpenAsar/arrpc/main/changelog.md");
rpm.version(find("(?m)^## v([\\d.]+)", md, 1));
if rpm.changed() {
	rpm.global("commit", gh_commit("OpenAsar/arrpc"));
}
