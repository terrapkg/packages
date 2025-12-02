let json = get(`https://api.github.com/repos/ad-oliviero/uwufetch/commits/development`).json();
let c = json.sha;
let d = json.commit.author.date;
rpm.global("commit", c);
if rpm.changed() {
    rpm.release();
    rpm.global("fulldate", d);
    d.truncate(10);
    let ver = gh_tag("ad-oliviero/uwufetch");
    rpm.global("ver", ver);
}
