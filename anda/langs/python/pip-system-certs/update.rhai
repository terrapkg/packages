rpm.global("pypi_version", pypi("pip-system-certs"));

if rpm.changed() {
    rpm.release();
}
