import "andax/bump_extras.rhai" as bump;
import "andax/spec.rhai" as spec;

let version = find(`version = "([\d.]+)"`, gh_rawfile("aya-rs/bpf-linker", "main", "Cargo.toml"), 1);
rpm.version(version);

let old_llvm_version = spec::get_global(#{
    f: open_file("anda/lib/bpf-linker/bpf-linker.spec").read_string()
}, "llvm_version");
let new_llvm_version = bump::bodhi("llvm", bump::as_bodhi_ver(labels.branch));
new_llvm_version.trim();
print(`bpf-linker updater: old LLVM=${old_llvm_version}`);
print(`bpf-linker updater: new LLVM=${new_llvm_version}`);
print(`bpf-linker updater: LLVM changed=${old_llvm_version != new_llvm_version}`);
rpm.global("llvm_version", new_llvm_version);

if old_llvm_version != new_llvm_version {
    let rel = spec::get_release(rpm).parse_int();
    rpm.release(rel + 1);
}
