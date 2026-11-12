// Follow the desktop release Flathub ships. Its manifest pins the online tag
// (coda-<version>-<tagrel>), and the branding tarball shares the version.
let manifest = gh_rawfile("flathub/com.collaboraoffice.Office", "master", "com.collaboraoffice.Office.json");
let tag = `"tag": "coda-([\d.]+)-(\d+)"`;
rpm.version(tag.find(manifest, 1));
rpm.global("tagrel", tag.find(manifest, 2));
