let v = gh("VOICEVOX/voicevox");
rpm.global("ver", v);
let engines = get(`https://raw.githubusercontent.com/VOICEVOX/voicevox/${v}/package.json`).json().engines;
rpm.global("nodev", find(">=([\\d.]+)", engines.node, 1));
rpm.global("npmv", find(">=([\\d.]+)", engines.npm, 1));
