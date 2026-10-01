rpm.version(find(`version: '([\d.]+)',`, gh_rawfile("quickjs-ng/quickjs", "master", "meson.build"), 1));
