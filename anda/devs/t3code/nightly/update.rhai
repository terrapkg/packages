let stable_ver = sh("grep -m1 '^Version:' anda/devs/t3code/stable/t3code.spec | sed -E 's/^Version:[[:space:]]*//'", #{"stdout": "piped"}).ctx.stdout;
stable_ver.trim();
let stable_ver_len = stable_ver.len();

let tags = gh_tags("pingdotgg/t3code");
tags.reverse();
for tag in tags {
    if tag.starts_with("v" + stable_ver + "-nightly.") {
        let nightly_parts = tag;
        nightly_parts.crop(1 + stable_ver_len + 9);
        let date_run = nightly_parts.split(".");

        let package_tag = tag;
        package_tag.crop(1);

        rpm.global("ver", stable_ver);
        rpm.global("date", date_run[0]);
        rpm.global("run", date_run[1]);
        rpm.global("tag", package_tag);
        break;
    }
}
