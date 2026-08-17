let dir = sub(`/[^/]+$`, "", __script_path);
sh(`../bootstrap/setup.sh fetch`, #{ "cwd": dir });
