import "andax/nvidia.rhai" as nvidia;

rpm.version(nvidia::nvidia_driver_version());

// Rebuild the package whenever the Alma kernel updates
let releasever = [];
for matches in find_all(`([\d]+\.[\d]+)/`, get("https://repo.almalinux.org/almalinux/")) {
        releasever += matches[1].parse_float();
}
releasever.dedup();
releasever.sort();
let kver = find(`kernel-([\d.]+.*?).x86_64.rpm`, get(`https://repo.almalinux.org/almalinux/${releasever[releasever.len()-1]}/BaseOS/x86_64/os/Packages/`), 1);
open_file("anda/system/nvidia/kmod-nvidia/VERSION_kernel.txt", "w").write(kver);
