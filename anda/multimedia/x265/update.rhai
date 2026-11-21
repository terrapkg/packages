let v = gh("Multicorewareinc/x265");
rpm.version(v);

if rpm.changed() {
    rpm.global("api_version", find(`set\(X265_BUILD ([\d]+)\)`, get(`https://raw.githubusercontent.com/Multicorewareinc/x265/refs/tags/${v}/source/CMakeLists.txt`), 1));
}
