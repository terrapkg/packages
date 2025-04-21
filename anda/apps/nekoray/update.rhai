rpm.version(find(`([\d.]+)-\d+-\d+-\d+`, gh_rawfile("Mahdi-zarei/nekoray", "dev", "nekoray_version.txt"), 1));

open_file("anda/apps/nekoray/Sagernet.SingBox.Version.txt", "w").write(gh('sagernet/sing-box'));
