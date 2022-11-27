let req = new_req("https://api.snapcraft.io/v2/snaps/info/authy");
req.head("Snap-Device-Series", "16");
let obj = json(req.get());
let obj2 = get_json(obj, "channel-map");
let obj3 = get_json(obj2, 0);
rpm.version(string_json(get_json(obj3, "version")));
