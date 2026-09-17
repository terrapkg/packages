import "andax/bump_extras.rhai" as bump;

rpm.version(bump::bodhi("glfw", bump::as_bodhi_ver(labels.branch)));