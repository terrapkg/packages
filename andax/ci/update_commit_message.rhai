import "anda::cfg" as cfg;

let cmd = `git status | sed -nE '/^\tmodified:/{s@^\tmodified:\s+@@;s@[^/]+$@@;p}' | sort -u`;
let filelist = sh(cmd, #{ "stdout": "piped" }).ctx.stdout.split('\n');

let modified_list = "";
for file in filelist {
	if file.is_empty() { continue; }
	let spec = cfg::load_file(`${file}/anda.hcl`).project.pkg.rpm.spec;
	spec.pop(5); // remove `.spec` suffix
	modified_list += `${spec} `;
}
print(modified_list[..modified_list.len()-1]);
