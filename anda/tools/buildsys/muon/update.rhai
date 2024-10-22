let versions = get("https://muon.build/releases/").json().keys();
versions.sort();
versions.pop();
rpm.version(versions.pop());
