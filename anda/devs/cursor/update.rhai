let data = get("https://www.cursor.com/api/download?platform=linux-x64&releaseTrack=stable").json();
rpm.version(data.version);
if rpm.changed() {
    rpm.global("commit", data.commitSha);
}
