let version = gh("adil192/shatter-shell");
rpm.version(version);
if !rpm.changed() {
    return;
}

let npm_sources = "# START NPM SOURCES\n";
let npm_caches = "# START NPM CACHE ADD\n";

let package_lock_json = gh_rawfile("adil192/shatter-shell", version, "package-lock.json");
let package_lock = from_json(package_lock_json);
let i = 100;
for info in package_lock.packages.values() {
    if ("os" in info && "linux" !in info.os){
        continue;
    }
    if ("resolved" !in info) {
        continue;
    }
    npm_sources += `Source${i}:      ${info.resolved}` + "\n";
    npm_caches += `%__npm cache add %{SOURCE${i}}` + "\n";
    i += 1;
}

fn replace_section(spec_content, start_string, end_string, section_content) {
    let start = spec_content.index_of(start_string);
    let end = spec_content.index_of(end_string);
    if (start == -1 || end == -1) {
        print(`Could not find ${start_string} and/or ${end_string}`);
        exit(1);
    }
    spec_content[0..start] + section_content + spec_content[end..]
}


let spec_content = rpm.f;
spec_content = replace_section(spec_content, "# START NPM SOURCES", "# END NPM SOURCES", npm_sources);
spec_content = replace_section(spec_content, "# START NPM CACHE ADD", "# END NPM CACHE ADD", npm_caches);
rpm.f = spec_content;
