// HACK: use RegEx to parse HTML!
let vers = find_all(`<a href="x265_([\d.]+).tar.gz"`, get("http://ftp.videolan.org/pub/videolan/x265/"));
// HACK: assume the last one is always the newest version!
let v = vers[vers.len()-1][1];
rpm.version(v);
// Best update script ever!!!!11

if rpm.changed() {
    rpm.global("api_version", find(`set\(X265_BUILD ([\d]+)\)`, get(`https://bitbucket.org/multicoreware/x265_git/raw/${v}/source/CMakeLists.txt`), 1));
}
