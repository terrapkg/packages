rpm.version(find(`nvm_echo \"v([\d.]+)\"`, gh_rawfile("nvm-sh/nvm", "master", "install.sh"), 1));
