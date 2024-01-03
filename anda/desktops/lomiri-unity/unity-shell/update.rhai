let html = get("http://archive.ubuntu.com/ubuntu/pool/universe/u/unity/?C=N;O=D");
let v = find("unity_([\\d.]+)\\+.+?.tar.xz", html, 1);
rpm.version(v);
rpm.define("archive", find("unity_([\\d.]+)\\+.+?.tar.xz", html, 0));
