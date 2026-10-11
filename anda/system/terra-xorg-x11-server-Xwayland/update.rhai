import "andax/bump_extras.rhai" as bump;

rpm.version(bump::bodhi("xorg-x11-server-Xwayland", bump::as_bodhi_ver(labels.branch)));
