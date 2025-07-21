rpm.global("commit", gh_commit("thestk/rtaudio"));
if rpm.changed() {
    let v = gh("thestk/rtaudio");
    v.crop(1);
	rpm.global("ver", v);
	rpm.global("commit_date", date());
}
