let surface = gh_tag("linux-surface/libwacom");
surface.crop(9);
rpm.global("surface_libwacom_ver", surface);

let upstream = find(`Version:        ([\d.]+)`, gh_rawfile("linux-surface/libwacom-surface", "master", "pkg/fedora/libwacom-surface.spec"), 1);
rpm.global("libwacom_ver", upstream);
