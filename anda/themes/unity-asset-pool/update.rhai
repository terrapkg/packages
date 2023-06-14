let html = get("https://launchpad.net/unity-asset-pool");
let v = find("Latest version is ([\\d.]+)", html, 1);
rpm.version(v);
let vs = v.split(".");
rpm.define("maj_min", `${vs[0]}.${vs[1]}`);
