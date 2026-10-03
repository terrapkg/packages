let tags = gh_tags("pingdotgg/t3code");
tags.reverse();
for tag in tags {
    if tag.starts_with("v") && tag.contains("-nightly.") {
        let package_tag = tag;
        package_tag.crop(1);

        let ver_and_build = package_tag.split("-nightly.");
        let date_run = ver_and_build[1].split(".");

        rpm.global("ver", ver_and_build[0]);
        rpm.global("date", date_run[0]);
        rpm.global("run", date_run[1]);
        rpm.global("tag", package_tag);
        break;
    }
}
