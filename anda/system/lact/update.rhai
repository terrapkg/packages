let r = get("https://api.github.com/repos/ilya-zlobintsev/LACT/tags").json_arr();

rpm.version(r[0].name);

if rpm.changed() {
  rpm.global("commit", r[0].commit.sha);
}
