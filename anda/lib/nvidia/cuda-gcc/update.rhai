import "andax/bump_extras.rhai" as bump;

rpm.version(bump::bodhi("gcc14", bump::as_bodhi_ver(labels.branch)));
