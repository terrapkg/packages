let url = `https://api.github.com/repos/ad-oliviero/uwufetch/commits/development`;
let c = json.sha;
let d = json.commit.author.date;
rpm.global("commit", c);
if rpm.changed() {
    rpm.release();
    rpm.global("fulldate", d);
    d.truncate(10);
    let ver = gh("ad-oliviero/uwufetch");
    ver.crop(1);
    rpm.global("ver", ver);
}
