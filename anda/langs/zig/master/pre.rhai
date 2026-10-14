import "andax/spec.rhai" as spec;

let v = spec::get_version(rpm);
let version = sub("~", "-", v);

let dir = sub(`/[^/]+$`, "", __script_path);
sh(`ZIG_VERSION=${version} ../setup.sh fetch`, #{ "cwd": dir });
