// Fetches the real upstream spec verbatim from the latest tag and replaces
// our local copy outright, instead of a %include curl-fetch at build time.
let tag = gh("CatPieLeaf/linux-p03");
rpm.f = get(`https://raw.githubusercontent.com/CatPieLeaf/linux-p03/${tag}/sources/kernel-p03/kernel-p03.spec`);
