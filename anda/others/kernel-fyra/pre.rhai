print("kernel-fyra: running pre.rhai");

// Install the kernel dependencies first
print(" $ sudo dnf5 -y builddep kernel");
sh_stdout("sudo dnf5 -y builddep kernel > OUT 2>&1");

// Install git for source and patchset retrieval
print(" $ sudo dnf5 -y install git");
sh_stdout("sudo dnf5 -y install git > OUT 2>&1");

// Run the actual build script
print(" $ ./build.sh");
sh_stdout("./build.sh 2>&1");

print("kernel-fyra: finished running pre.rhai");
