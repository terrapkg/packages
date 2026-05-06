let release = get(`https://api.github.com/repos/noctalia-dev/noctalia-qs/tags`).json_arr()[0];

rpm.version(release.name);

if rpm.changed() {
  rpm.global("commit", release.commit.sha);
}