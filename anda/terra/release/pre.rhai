let dir = sub(`/[^/]+$`, "", __script_path);

sh(`cp -p LICENSE -t ${dir}`, #{});
