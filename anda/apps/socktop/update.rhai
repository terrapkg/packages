rpm.global("ver", gh("jasonwitty/socktop"));
if rpm.changed() {
    rpm.release();
}
