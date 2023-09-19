print("kernel-fyra: running pre.rhai");

// Install the kernel dependencies first
print(" $ sudo dnf5 -y builddep kernel");
sh("sudo dnf5 -y builddep kernel > OUT 2>&1");
print(open_file("OUT").read());

// Install git for source and patchset retrieval
print(" $ sudo dnf5 -y install git");
sh("sudo dnf5 -y install git > OUT 2>&1");
print(open_file("OUT").read());

// Run the actual build script
print(" $ ./build.sh");
sh("./build.sh > OUT 2>&1");
print(open_file("OUT").read());

print("kernel-fyra: finished running pre.rhai");
