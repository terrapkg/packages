let v = find(`mesa-([\d.]+).tar.xz`, get("https://archive.mesa3d.org/?C=D;O=D"), 1);
rpm.version(v);
