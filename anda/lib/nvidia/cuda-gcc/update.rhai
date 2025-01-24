import "andax/bump_extras.rhai" as bump;

rpm.version(bump::bodhi("gcc13", labels.branch.as_bodhi_ver()));
