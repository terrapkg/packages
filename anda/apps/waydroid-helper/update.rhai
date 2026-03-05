rpm.version(`(?m)project\([^()]+^\s*version:\s*'([\d.]+)'[^()]+\)`.find(gh_rawfile("waydroid-helper/waydroid-helper", "main", "meson.build"), 1));
