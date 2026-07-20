let dir = sub(`/[^/]+$`, "", __script_path);
sh(`tar -czf keys.tar.gz RPM-GPG-KEY-terra*`, #{ "cwd": dir });
