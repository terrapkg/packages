rpm.version(gh("yt-dlp/yt-dlp-master-builds"));
if rpm.changed() {
    rpm.release();
}
