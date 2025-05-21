let v = (gitlab_tag("gitlab.winehq.org", "5"));
rpm.global("ver", v); // Sometimes the development branch includes RC candidates
if rpm.changed () {
    rpm.release();
    // Find the current highest release
    let matches = (find_all("[\\d.]+\\.[0x]", get("https://dl.winehq.org/wine/source/")));
    matches.dedup();
    let s = sh(`echo ${matches} | sed 's/,//g;s/\[//g;s/\]//g;s/"//g' | tr ' ' '\n' | sort -nr | tr '\n' ' '`, #{"stdout": "piped"}).ctx.stdout;
    s.truncate(4);
    rpm.global("srcmajor", s);
}
