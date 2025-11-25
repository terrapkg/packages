let mirrorlist = get("https://ziglang.org/download/community-mirrors.txt");
mirrorlist.pop();
let mirrors = sub("\n", " ", mirrorlist);
sh(`sed -i 's/mirrors=.*/mirrors="${mirrors}"/' anda/langs/zig/bootstrap/setup.sh`, #{});
sh(`anda/langs/zig/bootstrap/setup.sh fetch`, #{});
