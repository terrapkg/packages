import "andax/nvidia.rhai" as nvidia;

rpm.version(nvidia::nvidia_driver_version());

// Rebuild the package whenever the Alma kernel updates
let rawfile = get(`https://git.almalinux.org/rpms/kernel/raw/branch/a10s/kernel.spec`);
let kv = find("specrpmversion ([\\d.]+)", rawfile, 1);
let kr = find("specrelease ([\\d.]+)", rawfile, 1);
open_file("anda/system/nvidia/kmod-nvidia/KERNEL_VERSION.txt", "w").write(kv);
open_file("anda/system/nvidia/kmod-nvidia/KERNEL_RELEASE.txt", "w").write(kr);
