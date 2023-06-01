let release = gh("vinceliuice/Fluent-icon-theme")
rpm.global("tag", release);
rpm.version(sub("-", "", release));
