let regex = `<p>The latest version of chezmoi is ([\d.]+)`;
rpm.version(get("https://www.chezmoi.io").find(regex, 1));
