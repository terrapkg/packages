rpm.global("ver", gh("SevenTV/chatterino7").sub_string(1));
rpm.global("commit", gh_commit("SevenTV/chatterino7"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
}
