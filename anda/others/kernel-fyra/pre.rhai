print("kernel-fyra: running pre.rhai");

// Install the kernel dependencies first
print(" $ sudo dnf5 builddep kernel");
sh("sudo dnf5 builddep kernel > OUT 2>&1");
print(open_file("OUT").read_blob());

// Install git for source and patchset retrieval
print(" $ sudo dnf5 install git");
sh("sudo dnf5 install git > OUT 2>&1");
print(open_file("OUT").read_blob());

// Run the actual build script
print(" $ ./build.sh");
sh("./build.sh > OUT 2>&1");
print(open_file("OUT").read_blob());

print("kernel-fyra: finished running pre.rhai");
