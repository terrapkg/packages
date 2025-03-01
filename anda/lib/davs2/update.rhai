rpm.version(gh_tag("pkuvcl/davs2"));
if rpm.changed() {
    rpm.global("commit0", "%nil");
    rpm.release();
}