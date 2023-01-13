let obj = get("https://storage.googleapis.com/dart-archive/channels/stable/release/latest/VERSION").json();
rpm.version(obj.version);
