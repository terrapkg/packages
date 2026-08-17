import "anda::cfg" as cfg;

fn install(labels) {
    if labels.script_path == () {
        print("fatal: labels.script_path is empty");
        terminate();
    }
    let releasever = sh("rpm -E '%fedora'", #{"stdout": "piped"}).ctx.stdout;
    releasever.trim();
    let basearch = sh("rpm -E '%_arch'", #{"stdout": "piped"}).ctx.stdout;
    basearch.trim();
    let hcl = cfg::load_file(sub(`(.+/)[^.]+\.rhai`, "${1}anda.hcl", labels.script_path));
    for repo in hcl.project.pkg.rpm.extra_repos {
        repo = sub(`\$releasever`, releasever, repo);
        repo = sub(`\$basearch`, basearch, repo);
        let filename = sub(`\W`, "_", repo);
        let file = open_file(`/etc/yum.repos.d/${filename}.repo`);
        file.write(`
[filename]
name=${filename}
baseurl=${repo}
enabled=1
gpgcheck=0
`);
    }
}
