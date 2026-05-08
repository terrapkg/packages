rpm.global("commit", gh_commit("nats-io/natscli"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}