print("kernel-fyra: running pre.rhai");

// Install the kernel dependencies first
print(" $ sudo dnf5 -y builddep kernel");
print(sh("sudo dnf5 -y builddep kernel").sh_stdout());

// Install git for source and patchset retrieval
print(" $ sudo dnf5 -y install git");
print(sh("sudo dnf5 -y install git").sh_stdout());

// Run the actual build script
print(" $ ./build.sh");
print(sh("bash ./build.sh").sh_stdout());

print("kernel-fyra: finished running pre.rhai");
