rpm.version(find(`([\d.]+)-\d+-\d+-\d+`, gh_rawfile("throneproj/Throne", "dev", "throne_version.txt"), 1));

open_file("anda/apps/throne/Sagernet.SingBox.Version.txt", "w").write(gh("sagernet/sing-box"));
