import "andax/bump_extras.rhai" as bump;
import "andax/spec.rhai" as spec;

let version = find(`version = "([\d.]+)"`, gh_rawfile("aya-rs/bpf-linker", "main", "Cargo.toml"), 1);
rpm.version(version);

let old_llvm_version = spec::get_global(rpm, "llvm_version");
let new_llvm_version = "";
if labels.branch.starts_with("el") {
    new_llvm_version = bump::alma("llvm-devel", "AppStream", labels.branch);
} else {
    new_llvm_version = bump::bodhi("llvm", bump::as_bodhi_ver(labels.branch));
}
rpm.global("llvm_version", new_llvm_version);

if old_llvm_version != new_llvm_version {
    let rel = spec::get_release(rpm).parse_int();
    rpm.release(rel + 1);
}
