import "andax/nvidia.rhai" as nvidia;
let series = "9.6.0";
let url = `https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_${series}.json`;
let json = get(url).json();
rpm.version(json["cudnn"]["version"]);
