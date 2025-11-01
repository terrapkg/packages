// HACK: use RegEx to parse HTML!
let vers = find_all(`<a href="x265_([\d.]+).tar.gz"`, get("http://ftp.videolan.org/pub/videolan/x265/"));
// HACK: assume the last one is always the newest version!
rpm.version(vers[vers.len()-1][1]);
// Best update script ever!!!!11
