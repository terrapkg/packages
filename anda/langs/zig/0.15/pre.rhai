import "andax/spec.rhai" as spec;

let version = spec::get_version(rpm);

let dir = sub(`/[^/]+$`, "", __script_path);
sh(`ZIG_VERSION=${version} ../setup.sh fetch`, #{ "cwd": dir });
