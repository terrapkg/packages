// Only bumps the cache-buster %tag so Andaman's diff-based updater
// notices and rebuilds - the actual spec content is fetched live by
// the %include in apparmor.d-fedora.spec.
rpm.global("tag", gh("CatPieLeaf/apparmor.d-fedora"));
