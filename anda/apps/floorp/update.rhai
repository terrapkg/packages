let release_tag = gh("Floorp-Projects/Floorp");
let runtime_lock = gh_rawfile(
    "Floorp-Projects/Floorp",
    release_tag,
    "floorp-runtime.lock.json"
).json();

if runtime_lock.source.repository != "Floorp-Projects/Floorp-Runtime" {
    print(`floorp: unexpected runtime repository in ${release_tag} lock`);
    terminate();
}

rpm.version(release_tag);
rpm.global("runtime_commit", runtime_lock.source.commit);
