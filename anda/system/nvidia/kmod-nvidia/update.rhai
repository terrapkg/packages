import "andax/nvidia.rhai" as nvidia;

rpm.version(nvidia::nvidia_driver_version());

// Rebuild the package whenever the RHEL kernel updates
// The best we can do is track the kernel headers in UBI since they *should* reflect the kernel version RHEL is on
labels.branch.crop(2);
let html = get(`https://cdn-ubi.redhat.com/content/public/ubi/dist/ubi${labels.branch}/${labels.branch}/x86_64/appstream/os/Packages/k/`);
let kver = find(`kernel-headers-([\d.]+.*?).x86_64.rpm`, html, 1);
open_file("anda/system/nvidia/kmod-nvidia/VERSION_kernel.txt", "w").write(kver);
