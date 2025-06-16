fn get_version() {
    return `(?m)^Version:\s*(.+)$`.find(this.f, 1);
}

fn get_release() {
    let r = `(?m)^Release:\s*(.+)$`.find(this.f, 1);
    r = sub(`(?m)(%\??dist|%\{\??dist\})\s*$`, "", r);
    r.replace("%autorelease", "1");
    return r;
}

/// Only supports one-liner `%global`s!
fn get_global(macro) {
    return `(?m)^%global\s+${macro}\s+(.+)$`.find(this.f, 1);
}

/// Only supports one-liner `%define`s!
fn get_define(macro) {
    return `(?m)^%define\s+${macro}\s+(.+)$`.find(this.f, 1);
}

fn get_version(rpm) { rpm.get_version() }
fn get_release(rpm) { rpm.get_release() }
fn get_global(rpm, macro) { rpm.get_global(macro) }
fn get_define(rpm, macro) { rpm.get_define(macro) }
