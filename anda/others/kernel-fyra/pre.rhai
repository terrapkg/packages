// Install the kernel dependencies first
sh("sudo dnf5 builddep kernel");

// Install git for source and patchset retrieval
sh("sudo dnf5 install git");

// Run the actual build script
sh("build.sh");