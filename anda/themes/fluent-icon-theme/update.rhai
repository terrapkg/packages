let release = gh("vinceliuice/Fluent-icon-theme")
rpm.global("commit", sha);
rpm.version(sub("-", "", release));
