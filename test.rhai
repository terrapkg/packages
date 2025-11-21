let mirrorlist = get("https://ziglang.org/download/community-mirrors.txt");
mirrorlist.pop();
let mirrors = mirrorlist.split('\n');
let stdout = sh(`echo $((RANDOM % ${mirrors.len()}))`, #{ "stdout": "piped" }).ctx.stdout;
stdout.trim();
let mirror = mirrors[parse_int(stdout)];

print(mirror);
