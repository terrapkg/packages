let html = get("https://app-updates.agilebits.com/product_history/CLI2");
let versions = [];

for matches in find_all(`op_linux_amd64_v([\d]+\.[\d]+\.[\d]+)\.zip`, html) {
    versions += matches[1];
}

versions.dedup();

let latest = "";
let latest_major = 0;
let latest_minor = 0;
let latest_patch = 0;

for version in versions {
    let parts = version.split(".");
    let major = parts[0].parse_int();
    let minor = parts[1].parse_int();
    let patch = parts[2].parse_int();

    if latest == "" ||
        major > latest_major ||
        major == latest_major && minor > latest_minor ||
        major == latest_major && minor == latest_minor && patch > latest_patch {
        latest = version;
        latest_major = major;
        latest_minor = minor;
        latest_patch = patch;
    }
}

if latest == "" {
    print("E: no 1Password CLI version found");
    terminate();
}

rpm.version(latest);
