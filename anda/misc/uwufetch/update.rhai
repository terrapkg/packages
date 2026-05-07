let json = get(`https://api.github.com/repos/ad-oliviero/uwufetch/commits/development`).json();
let c = json.sha;
let d = json.commit.author.date;
d.truncate(10);
rpm.global("commit", c);
if rpm.changed() {
    rpm.release();
    rpm.global("fulldate", d);
    let ver = gh_tag("ad-oliviero/uwufetch");
    rpm.global("ver", ver);
}
