let staging = get("https://gitlab.winehq.org/api/v4/projects/231/repository/tags").json_arr()[0].tag_name;
staging.crop(1);
let f = rpm.f;
rpm.global("staging_version", staging);
rpm.global("tkg_version", gh("Frogging-Family/wine-tkg-git"))

if f != rpm.f {
	rpm.release("1%{?wine_tkg:.wine_tkg}");
}
