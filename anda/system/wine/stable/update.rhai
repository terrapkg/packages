let matches = (find_all("[\\d.]+[.]0", get("https://dl.winehq.org/wine/source/"))); // Only find versions ending in .0. Stable WINE always ends in .0
matches.dedup();
// Sort for the largest match, the sed and tr commands remove everything preventing sort from working correctly
let v = sh(`echo ${matches} | sed 's/,//g' | sed 's/\[//g' | sed 's/\]//g' | sed 's/"//g' | tr ' ' '\n' | sort -nr | tr '\n' ' '`, #{"stdout": "piped"}).ctx.stdout;
v.truncate(4);
rpm.version(v);
