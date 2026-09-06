rpm.global("commit", codeberg_commit("nathandyer/exquisite-linux-templates"));
if rpm.changed() {
    rpm.global("commit_date", date());
}
