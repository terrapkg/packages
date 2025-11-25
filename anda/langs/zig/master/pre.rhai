let dir = sub(`/[^/]+$`, "", __script_path);
sh(`${dir}/setup.sh fetch`, #{ "cwd": dir });
