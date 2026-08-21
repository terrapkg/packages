rpm.global("tag", gh_tag("project-repo/cagebreak"));

if rpm.changed() {
    rpm.release();
}
