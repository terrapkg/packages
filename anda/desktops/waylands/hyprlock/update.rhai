let v = gh_rawfile("hyprwm/hyprlock", "main", "VERSION");
v.trim();
rpm.version(v);
