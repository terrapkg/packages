let series = "0.6.3";
let url = `https://developer.download.nvidia.com/compute/cusparselt/redist/redistrib_${series}.json`;
let json = get(url).json();

rpm.version(json["libcusparse_lt"]["version"]);
