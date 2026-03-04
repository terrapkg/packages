let url = "https://developer.download.nvidia.com/compute/cusparselt/redist/";
let matches = find_all("redistrib_[\\d.]+.json", get(url));
let series = `${url}${matches[matches.len - 1][0]}`;
let json = get(series).json();
rpm.version(json["libcusparse_lt"]["version"]);
