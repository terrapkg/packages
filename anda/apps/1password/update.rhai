let xml = get("https://releases.1password.com/linux/stable/index.xml");

let latest = "";
let latest_major = 0;
let latest_minor = 0;
let latest_patch = 0;

for title in find_all(`<title>[^<]*</title>`, xml) {
    let matches = find_all(`[\d]+\.[\d]+\.[\d]+`, title[0]);
    if matches.len() == 0 {
        continue;
    }

    let version = matches[0][0];
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
    print("E: no 1Password version found");
    terminate();
}

rpm.version(latest);
