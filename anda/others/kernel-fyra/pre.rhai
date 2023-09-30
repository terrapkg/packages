print("kernel-fyra: running pre.rhai");

// Install the kernel dependencies first
print(" $ sudo dnf5 -y builddep kernel");
print(sh("sudo dnf5 -y builddep kernel").sh_stdout());

// Install git for source and patchset retrieval
print(" $ sudo dnf5 -y install git");
print(sh("sudo dnf5 -y install git").sh_stdout());

// Run the actual build script
print(" $ ./build.sh");
let cmd = sh("./anda/others/kernel-fyra/build.sh");
print(cmd.sh_stdout());
let err = cmd.sh_stderr();
if !err.is_empty() {
  print("STDERR:");
  print(err);
}

print("kernel-fyra: finished running pre.rhai");
