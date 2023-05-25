let txt = get("https://gitlab.gnome.org/api/v4/projects/665/repository/tags");
for item in txt.json_arr() {
	if item.name.starts_with("4.") {
		rpm.version(item.name);
		break;
	}
}
