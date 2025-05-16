let v = (gitlab_tag("gitlab.winehq.org", "5"));
v.crop(1);
rpm.global("ver", v); // Sometimes the development branch includes RC candidates
if rpm.changed () {
    rpm.release();
    // Only find versions ending in .x (point releases)
    let matches = (find_all("[\\d.]+[.]x", get("https://dl.winehq.org/wine/source/")));
    matches.dedup();
    let s = sh(`echo ${matches} | sed 's/,//g' | sed 's/\[//g' | sed 's/\]//g' | sed 's/"//g' | tr ' ' '\n' | sort -nr | tr '\n' ' '`, #{"stdout": "piped"}).ctx.stdout;
    s.truncate(4);
    rpm.global("srcmajor", s);
}
