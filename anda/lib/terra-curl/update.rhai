let latest_tag = gh_tag("curl/curl");

// Convert tag like "rc-8_21_0-2" → "8.21.0~rc2"
// or like "8_21_0" → "8.21.0"
let version;
if latest_tag.starts_with("rc-") {
    version = sub("rc-(\\d+)_(\\d+)_(\\d+)-(\\d+)", "${1}.${2}.${3}~rc${4}", latest_tag);
} else {
    version = sub("(\\d+)_(\\d+)_(\\d+)", "${1}.${2}.${3}", latest_tag);
}

rpm.version(version);
