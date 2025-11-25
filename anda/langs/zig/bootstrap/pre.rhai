let mirrorlist = get("https://ziglang.org/download/community-mirrors.txt");
mirrorlist.pop();
let mirrors = sub("\n", " ", mirrorlist);
sh(`sed -i 's/mirrorlist=.*/mirrorlist=\\"${mirrors}\\"/' anda/langs/zig/bootstrap/setup.sh`, #{});

let dir = sub(`/[^/]+$`, "", __script_path);
sh(`./setup.sh fetch`, #{ "cwd": dir });
