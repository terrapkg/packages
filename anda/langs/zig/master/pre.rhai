let mirrorlist = get("https://ziglang.org/download/community-mirrors.txt");
mirrorlist.pop();
let mirrors = mirrorlist.split('\n');
let stdout = sh(`echo $((RANDOM % ${mirrors.len()}))`, #{ "stdout": "piped" }).ctx.stdout;
stdout.trim();
let mirror = mirrors[parse_int(stdout)];

let dir = sub(`/[^/]+$`, "", __script_path);
let ver = `(?m)^Version:\s*(.+)$`.find(open_file(`${dir}/zig-master.spec`).read_string(), 1);
ver = sub("~", "-", ver);

sh(`wget ${mirror}/zig-${ver}.tar.xz ${mirror}/zig-${ver}.tar.xz.minisig`, #{ "cwd": dir });
