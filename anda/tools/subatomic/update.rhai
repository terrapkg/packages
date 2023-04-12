let sha = get("https://api.github.com/repos/FyraLabs/subatomic/commits").json_arr()[0].sha;
rpm.global("commit", sha);
