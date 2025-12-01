import "andax/bump_extras.rhai" as bump;
import "andax/spec.rhai" as spec;

let v = bump::madoguchi("nvidia-kmod-common", labels.branch);
let m = gh("NVIDIA/open-gpu-kernel-modules");
if m == v {
    rpm.version(v);
}

// Rebuild the package whenever the Alma kernel updates
let releasever = labels.branch;
releasever.crop(2);
let majorminor = [];
for matches in find_all(`(${releasever}\.[\d]+)/`, get("https://repo.almalinux.org/almalinux/")) {
        majorminor += matches[1].parse_float();
}
majorminor.dedup();
majorminor.sort();
let kver = find_all(`kernel-([\d.]+.*?)\.el.*?\.x86_64\.rpm`, get(`https://repo.almalinux.org/almalinux/${majorminor[majorminor.len()-1]}/BaseOS/x86_64/os/Packages/`));
kver.dedup();
open_file("anda/system/nvidia/kmod-nvidia/VERSION_kernel.txt", "w").write(`${kver[kver.len - 1][1]}`);

let dir = sub(`/[^/]+$`, "", __script_path);
if sh("[[ `git status " + dir + " --porcelain` ]] && exit 1 || exit 0", #{}).ctx.rc == 1 {
    let rel = spec::get_release(rpm).parse_int();
    rpm.release(rel + 1);
}
