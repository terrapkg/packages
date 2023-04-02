let html = get("http://archive.ubuntu.com/ubuntu/pool/universe/u/unity-greeter/?C=N;O=D");
let v = find("unity-greeter_([\\d.+]+)-0ubuntu2", html, 1);
rpm.version(v);
