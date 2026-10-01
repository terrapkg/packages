// Temporarily pin cargo-about to Zed's compatible version until upstream fixes their stuff.

// rpm.version(crates("cargo-about"));

rpm.version(find(`CARGO_ABOUT_VERSION="([\d.]+)"`, gh_rawfile("zed-industries/zed", "main", "script/generate-licenses"), 1));
