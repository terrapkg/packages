let req = new_req("https://api.snapcraft.io/v2/snaps/info/authy");
req.head("Snap-Device-Series", "16");
let obj = json(req.get())["channel-map"][0];
rpm.version(obj.version);
rpm.source(0, obj.download.url);
