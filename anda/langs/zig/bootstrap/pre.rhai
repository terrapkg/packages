let dir = sub(`/[^/]+$`, "", __script_path);
sh(`./setup.sh fetch`, #{ "cwd": dir });
