fn get_version(rpm) {
    return `(?m)^Version:\s*(.+)$`.find(rpm.f, 1);
}

fn get_release(rpm) {
    let r = `(?m)^Release:\s*(.+)$`.find(rpm.f, 1);
    r = sub(`(?m)(%\??dist|%\{\??dist\})\s*$`, "", r);
    r.replace("%autorelease", "1");
    return r;
}

/// Only supports one-liner `%global`s!
fn get_global(rpm, macro) {
    return `(?m)^%global\s+${macro}\s+(.+)$`.find(rpm.f, 1);
}

/// Only supports one-liner `%define`s!
fn get_define(rpm, macro) {
    return `(?m)^%define\s+${macro}\s+(.+)$`.find(rpm.f, 1);
}

fn bump_release(rpm) {
    rpm.release(`${rpm.get_release().parse_int() + 1}`);
}
