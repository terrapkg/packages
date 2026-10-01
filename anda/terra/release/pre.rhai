let dir = sub(`/[^/]+$`, "", __script_path);

sh(`cp -pv LICENSE -t ${dir}`, #{});
