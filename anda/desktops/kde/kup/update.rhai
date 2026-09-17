let v = gitlab_tag("invent.kde.org", "445");
rpm.global("ver", v);
if rpm.changed() {
    rpm.global("commit", get(`https://invent.kde.org/api/v4/projects/445/repository/tags/${v}`).json().commit.id);
}
