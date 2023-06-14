let html = get("http://archive.ubuntu.com/ubuntu/pool/universe/c/compiz/?C=N;O=D");
let v = find("compiz_([\\d.]+)\\+(.+?).tar.xz", html, 1);
let r = find("compiz_([\\d.]+)\\+(.+?).tar.xz", html, 2);
rpm.version(v);
rpm.define("_ubuntu_rel", r);
