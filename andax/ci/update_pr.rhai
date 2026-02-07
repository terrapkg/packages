import "anda::cfg" as cfg;

fn pr(branch, dir, spec) {
	sh(`git checkout ${branch}`, #{});
	if sh(`git stash apply`, #{}).ctx.rc != 0 {
		sh(`git reset HEAD ${dir}`, #{});
		return;
	}
	if sh(`git commit -S -m "bump(${labels.scope}): ${spec}" ${dir}`, #{}).ctx.rc != 0 {
		sh(`git reset HEAD ${dir}`, #{});
		return;
	}
	sh(`gh pr create --title '[${branch}] bump(${labels.scope}): ${spec}' --body 'Automatic bump from CI\n\nnosync'`, #{});
	sh(`git reset --hard HEAD^`, #{});
}

let cmd = `git status | sed -nE '/^\tmodified:/{s@^\tmodified:\s+@@;s@[^/]+$@@;p}' | sort -u`;
let filelist = sh(cmd, #{ "stdout": "piped" }).ctx.stdout.split('\n');

for dir in filelist {
	if dir.is_empty() { continue; }
	let spec = cfg::load_file(`${dir}/anda.hcl`).project.pkg.rpm.spec;
	spec.pop(5); // remove `.spec` suffix
	if labels.scope == "branch" {
		sh(`git commit -S -m "bump(${labels.scope}): ${spec}" ${dir}`, #{});
		continue;
	}
	sh(`git stash push -m "bump(${labels.scope}): ${spec}" -- ${dir}`, #{});
	pr("frawhide", dir, spec);
	pr("f43", dir, spec);
	pr("f42", dir, spec);
	pr("el10", dir, spec);
	sh(`git stash drop`, #{});
}
