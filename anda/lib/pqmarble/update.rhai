let req = get("https://gitlab.gnome.org/api/v4/projects/20662/repository/branches/master").json();
rpm.global("commit", req.commit.id);
let meson = get("https://gitlab.gnome.org/raggesilver/marble/-/raw/master/meson.build");
rpm.global("ver", find("(?m)^\\s+version:\\s*'(.+)',$", meson, 1));
