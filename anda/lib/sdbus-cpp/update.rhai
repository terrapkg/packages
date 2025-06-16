rpm.version(`(?m)^project\(sdbus-c\+\+ VERSION ([\d.]+) LANGUAGES CXX C\)$`.find(gh_rawfile("Kistler-Group/sdbus-cpp", "master", "CMakeLists.txt"), 1));
