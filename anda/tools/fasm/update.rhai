let content = get("https://raw.githubusercontent.com/tgrysztar/fasm/master/SOURCE/VERSION.INC");
let version = find("VERSION_STRING equ \"(\\d+\\.\\d+\\.\\d+)\"", content, 1);
rpm.version(version);
