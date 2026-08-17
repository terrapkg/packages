let v = gh("OpenGamingCollective/cardwire");
rpm.version(v);
if rpm.changed() {
  rpm.global("cardwire_toolchain", `const\s+EBPF_NIGHTLY[^"]+"([^"]+)"`.find(gh_rawfile("OpenGamingCollective/cardwire", v, 1)));
}
