let o = get("https://gitlab.com/api/v4/projects/25716028/repository/tags").json_arr()[0];
rpm.version(o.name);
rpm.global("commit", get("https://gitlab.com/api/v4/projects/25716028/repository/commits").json_arr()[0].id);
