rpm.global("commit", gh_commit("noctalia-dev/noctalia-greeter"));
if rpm.changed() {
        rpm.global("ver", `(?m)^\s*version:\s*'([\d\.]+)',$`.find(gh_rawfile("noctalia-dev/noctalia-greeter", "main", "meson.build"), 1));
        rpm.global("commit_date", date());
        rpm.release();
}
