print("kernel-fyra: running pre.rhai");

// Install the kernel dependencies first
print(" $ sudo dnf5 builddep kernel > $OUT 2>&1");
sh("sudo dnf5 builddep kernel > $OUT 2>&1");
print(env("OUT"));

// Install git for source and patchset retrieval
print(" $ sudo dnf5 install git > $OUT 2>&1");
sh("sudo dnf5 install git > $OUT 2>&1");
print(env("OUT"));

// Run the actual build script
print(" $ ./build.sh");
sh("./build.sh > $OUT 2>&1");
print(env("OUT"));

print("kernel-fyra: finished running pre.rhai");
