let upstream = get(`https://src.fedoraproject.org/rpms/fcitx5-mozc/raw/rawhide/f/fcitx5-mozc.spec`);
rpm.global("version0", find(`(?m)^%global\s+version0\s+(\S+)$`, upstream, 1));
