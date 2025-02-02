import "andax/bump_extras.rhai" as bump;

rpm.version(bump::bodhi("gcc13", bump::as_bodhi_ver(labels.branch)));
