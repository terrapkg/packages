import "andax/bump_extras.rhai" as bump;

rpm.version(bump::bodhi("fdk-aac-free", bump::as_bodhi_ver(labels.branch)));
