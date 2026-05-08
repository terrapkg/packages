import "andax/bump_extras.rhai" as bump;

if labels.branch >= "F42" {
    rpm.version(bump::bodhi("gcc14", bump::as_bodhi_ver(labels.branch)));
} else {
    rpm.version(bump::bodhi("gcc13", bump::as_bodhi_ver(labels.branch)));
}
