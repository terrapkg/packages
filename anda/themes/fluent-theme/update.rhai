let release = gh("vinceliuice/Fluent-gtk-theme")
rpm.global("tag", release);
rpm.version(sub("-", "", release));
