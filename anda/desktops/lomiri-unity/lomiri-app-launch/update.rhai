rpm.version(get("https://gitlab.com/api/v4/projects/17286402/repository/tags").json_arr()[0].name);
rpm.global("commit", get("https://gitlab.com/api/v4/projects/17286402/repository/commits").json_arr()[0].id);
