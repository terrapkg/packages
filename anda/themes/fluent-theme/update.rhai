let release = gh("vinceliuice/Fluent-gtk-theme")
rpm.global("commit", sha);
rpm.version(sub("-", "", release));
