// Fetches the real upstream spec verbatim from the latest tag and replaces
// our local copy outright, instead of a %include curl-fetch at build time.
// Version/Release are baked into that upstream file already (tag_release
// global, Source0 pinned to the same tag), so there's nothing else to bump
// here - the whole-file replace is what keeps this in sync automatically.
let tag = gh("CatPieLeaf/apparmor.d-fedora");
rpm.f = get(`https://raw.githubusercontent.com/CatPieLeaf/apparmor.d-fedora/${tag}/dists/apparmor.d-fedora.spec`);
