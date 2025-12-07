import "andax/bump_extras.rhai" as bump;
import "andax/spec.rhai" as spec;

let v = bump::madoguchi("nvidia-kmod-common", labels.branch);
let m = gh("NVIDIA/open-gpu-kernel-modules");
if m == v {
    rpm.version(v);
}

// Rebuild the package whenever the Alma kernel updates
let kver = bump::alma_vr("kernel", "BaseOS", labels.branch)[1];
let krel = bump::alma_vr("kernel", "BaseOS", labels.branch)[2];
open_file("anda/system/nvidia/kmod-nvidia/VERSION_kernel.txt", "w").write(kver);
open_file("anda/system/nvidia/kmod-nvidia/RELEASE_kernel.txt", "w").write(krel);

let dir = sub(`/[^/]+$`, "", __script_path);
if sh("[[ `git status " + dir + " --porcelain` ]] && exit 1 || exit 0", #{}).ctx.rc == 1 {
    let rel = spec::get_release(rpm).parse_int();
    rpm.release(rel + 1);
}
