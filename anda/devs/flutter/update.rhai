let obj = get("https://storage.googleapis.com/flutter_infra_release/releases/releases_linux.json").json();
for release in obj.releases {
  if release.channel == "stable" {
    rpm.version(release.version);
    break;
  }
}
