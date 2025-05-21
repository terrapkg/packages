import "andax/nvidia.rhai" as nvidia;

rpm.version(nvidia::nvidia_driver_version());

// Rebuild the package whenever the RHEL kernel updates
// The best we can do is track the kernel headers in UBI since they *should* reflect the kernel version RHEL is on
// Track both architectures we support since release can be bumped on either

let html1 = get("https://cdn-ubi.redhat.com/content/public/ubi/dist/ubi10/10/x86_64/appstream/os/Packages/k/");
let html2 = get("https://cdn-ubi.redhat.com/content/public/ubi/dist/ubi10/10/aarch64/appstream/os/Packages/k/");
let kver_x64 = find(`kernel-headers-([\d.]+.*?).x86_64.rpm`, html1, 1);
let kver_arm64 = find(`kernel-headers-([\d.]+.*?).aarch64.rpm`, html2, 1);
open_file("anda/system/nvidia/kmod-nvidia/KERNEL_x86_64.txt", "w").write(kver_x64);
open_file("anda/system/nvidia/kmod-nvidia/KERNEL_aarch64.txt", "w").write(kver_arm64);
