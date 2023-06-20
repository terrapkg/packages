// let v = gh("VOICEVOX/voicevox");
// rpm.version(v);
// let engines = get(`https://raw.githubusercontent.com/VOICEVOX/voicevox/${v}/package.json`).json().engines;
// rpm.define("nodev", find(">=([\\d.]+)", engines.node, 1));
// rpm.define("nodev", find(">=([\\d.]+)", engines.npm, 1));
let v = "0.14.7";
let engines = get(`https://raw.githubusercontent.com/VOICEVOX/voicevox/${v}/package.json`).json().engines;
print(find(">=([\\d.]+)", engines.node, 1));
print(find(">=([\\d.]+)", engines.npm, 1));
