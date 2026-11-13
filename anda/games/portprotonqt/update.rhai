rpm.version(gitea("git.linux-gaming.ru", "Linux-Gaming/PortProtonQt"));
if rpm.changed() {
    rpm.release();
}
