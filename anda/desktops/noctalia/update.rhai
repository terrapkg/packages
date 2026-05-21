let commit = get(`https://api.github.com/repos/noctalia-dev/noctalia-qs/commits?sha=v5`).json_arr()[0];

rpm.global("commit", release.sha);
