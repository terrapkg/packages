let html = get("http://archive.ubuntu.com/ubuntu/pool/universe/g/glewmx/?C=N;O=D");
let v = find("glewmx_([\\d.+]+).", html, 1);
rpm.version(v);
