let obj = get("https://pypi.org/pypi/python3-protobuf/json").json();
rpm.version(obj @ "info" @ "version");
