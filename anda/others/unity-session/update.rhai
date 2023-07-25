let html = get("http://archive.ubuntu.com/ubuntu/pool/universe/g/gnome-session/?C=N;O=D");
let v = find("unity-session_([\\d.]+)-(.+?)_all.deb", html, 1);
let r = find("unity-session_([\\d.]+)-(.+?)_all.deb", html, 2);
rpm.version(v);
rpm.define("_ubuntu_rel", r);
