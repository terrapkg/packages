import "andax/bump_extras.rhai" as bump;

rpm.version(bump::bodhi("openh264", bump::as_bodhi_ver(labels.branch)));
