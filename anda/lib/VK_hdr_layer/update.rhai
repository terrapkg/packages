rpm.global("commit", gh_commit("zamundaaa/VK_hdr_layer"));
if rpm.changed() {
    rpm.release();
    rpm.global("commitdate", date());
}
