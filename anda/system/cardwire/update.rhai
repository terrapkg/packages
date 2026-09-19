let v = gh("OpenGamingCollective/cardwire");
rpm.version(v);
if rpm.changed() {
  rpm.global("cardwire_toolchain", find(`const\s+EBPF_NIGHTLY[^"]+"([^"]+)"`, gh_rawfile("OpenGamingCollective/cardwire", v, "crates/cardwire-ebpf-userspace/build.rs"), 1));
}
