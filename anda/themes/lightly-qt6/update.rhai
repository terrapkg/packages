let repos = get("https://repology.org/api/v1/project/qt").json_arr();
let branch = sh("git rev-parse --abbrev-ref HEAD", #{"stdout": "piped"}).ctx.stdout;
branch.crop(1);
branch.trim();
let vers = repos.filter(|r| r.repo == `fedora_${branch}`).map(|r| [find("^(\\d+)\\.(\\d+)\\..+$", r.version, 1), find("^(\\d+)\\.(\\d+)\\..+$", r.version, 2)]);
let ver = vers.find(|v| v[0] == "6")[1]; // assume there is only 1 package for v6.x
open_file("anda/themes/lightly-qt6/VER6.txt").write(`${ver}`); // will trig rebuild when changed
