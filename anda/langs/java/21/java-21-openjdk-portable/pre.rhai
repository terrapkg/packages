let dir = sub(`/[^/]+$`, "", __script_path);

sh(`fetch-icedtea --branch 6.0`, #{ "cwd": dir });
