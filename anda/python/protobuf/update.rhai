let obj = get("https://pypi.org/pypi/protobuf/json").json();
rpm.version(obj @ "info" @ "version");
