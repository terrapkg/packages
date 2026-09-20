import "andax/bump_extras.rhai" as bump;
import "andax/spec.rhai" as spec;

if labels.branch.starts_with("el") {
    rpm.global("llvm_version", bump::alma("llvm-devel", "AppStream", labels.branch));
} else {
    rpm.global("llvm_version", bump::bodhi("llvm", bump::as_bodhi_ver(labels.branch)));
}

if rpm.changed() {
    let rel = spec::get_release(rpm).parse_int();
    rpm.release(rel + 1);
}

let version = find(`version = "([\d.]+)"`, gh_rawfile("aya-rs/bpf-linker", "main", "Cargo.toml"), 1);
rpm.version(version);
