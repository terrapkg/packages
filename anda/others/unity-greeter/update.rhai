let html = get("http://archive.ubuntu.com/ubuntu/pool/universe/u/unity-greeter/?C=N;O=D");
let v = find("unity-greeter_([\\d.+]+)-0ubuntu(\d\+)", html, 1);
let rn = find("unity-greeter_([\\d.+]+)-0ubuntu(\d\+)", html, 2);
rpm.version(v);
rpm.global("rn", rn);
