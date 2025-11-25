let dir = sub(`/[^/]+$`, "", __script_path);
sh(`anda/langs/zig/master/setup.sh fetch`, #{ "cwd": dir });
