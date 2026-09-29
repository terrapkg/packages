let upstream = find(`Version:        ([\d.]+)`, gh_rawfile("Ultramarine-Linux/libwacom-surface", "master", "pkg/fedora/libwacom-surface.spec"), 1);
rpm.global("libwacom_ver", upstream);
