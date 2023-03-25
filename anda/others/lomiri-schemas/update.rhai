let o = get("https://gitlab.com/api/v4/projects/30932494/repository/tags").json_arr()[0];
rpm.global("commit", o.commit.id);
rpm.version(o.name);
