rpm.version(find(`\"name\":\"Linux\",\"latestVersion\":\"([\d.]+)\"`, get(`https://www.videolan.org/vlc/`), 1));
