let req = new_req("https://gitlab.gnome.org/api/v4/projects/1551/repository/branches/main");
rpm.global("commit", json(req.get()).commit.id)
