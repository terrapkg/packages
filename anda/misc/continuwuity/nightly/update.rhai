rpm.global("ver", get("https://forgejo.ellis.link/api/v1/repos/continuwuation/continuwuity/releases?pre-release=true").json.tag_name);
rpm.global("commit", get("https://forgejo.ellis.link/api/v1/repos/continuwuation/continuwuity/commits?limit=1").json_arr()[0].sha);
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
}
