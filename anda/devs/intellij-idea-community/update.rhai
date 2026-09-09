let ver = gh_tag("JetBrains/intellij-community");
let ver2 = gh_tag("JetBrains/android");
if ver.starts_with("idea/") && ver == ver2 {
	ver.remove("idea/");
	rpm.version(ver);
}
