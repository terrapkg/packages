let v = [];
// Only find versions ending in .0. Stable WINE always ends in .0
for matches in find_all("[\\d.]+\\.0", get("https://dl.winehq.org/wine/source/")) {
        v += matches[0].parse_float();
}
v.dedup();
v.sort();
rpm.version(v[v.len()-1]);
