let r = get("https://api.github.com/repos/ghostty-org/ghostty/releases/83450291").json();
let d = sh(`date -d "${r.created_at}" "+%Y%m%d%H%M"`, #{"stdout": "piped"}).ctx.stdout;
d.pop();

print(d);
