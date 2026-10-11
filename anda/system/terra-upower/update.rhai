import "andax/bump_extras.rhai" as bump;

rpm.version(bump::bodhi("upower", bump::as_bodhi_ver(labels.branch)));
