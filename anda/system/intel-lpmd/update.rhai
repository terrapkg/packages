rpm.version(`(?m)^### Release ([\d.]+)$`.find(gh_rawfile("intel/intel-lpmd", "main", "README.md"), 1));
