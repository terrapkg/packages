let v = gh("VOICEVOX/voicevox");
rpm.version(v);
let engines = get(`https://raw.githubusercontent.com/VOICEVOX/voicevox/${v}/package.json`).json().engines;
rpm.define("nodev", find(">=([\\d.]+)", engines.node, 1));
rpm.define("npmv", find(">=([\\d.]+)", engines.npm, 1));
