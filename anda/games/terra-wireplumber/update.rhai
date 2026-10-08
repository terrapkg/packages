import "andax/bump_extras.rhai" as bump;

rpm.version(bump::bodhi("wireplumber", bump::as_bodhi_ver(labels.branch)));
