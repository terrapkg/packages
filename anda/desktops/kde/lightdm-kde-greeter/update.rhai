let v = gitlab_tag("invent.kde.org", "2512");
rpm.version(v);
if rpm.changed() {
    rpm.global("commit", get(`https://invent.kde.org/api/v4/projects/2512/repository/tags/${v}`).json().commit.id);
}
