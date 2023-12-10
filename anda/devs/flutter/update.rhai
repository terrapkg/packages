let obj = get("https://storage.googleapis.com/flutter_infra_release/releases/releases_linux.json").json();
rpm.version(obj.releases[0].version);
