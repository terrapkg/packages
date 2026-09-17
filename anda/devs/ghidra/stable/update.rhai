let tag = gh_tag("NationalSecurityAgency/ghidra");
let v  = find(`Ghidra_([\d.]+)_build`, tag, 1);
rpm.version(v);

if rpm.changed() {
  let rawfile = gh_rawfile("NationalSecurityAgency/ghidra", tag, "gradle/support/fetchDependencies.gradle");

  let yajsw_ver  = find(`yajsw-stable-([\d.]+)\.zip`, rawfile, 1);
  rpm.global("yajsw_ver", yajsw_ver);

  let pydev_ver  = find(`PyDev ([\d.]+)\.zip`, rawfile, 1);
  rpm.global("pydev_ver", pydev_ver);

  let cdt_ver  = find(`cdt-([\d.]+)\.zip`, rawfile, 1);
  rpm.global("cdt_ver", cdt_ver);

  let sarif_ver  = find(`java-sarif-([\d.]+)-modified\.jar`, rawfile, 1);
  rpm.global("sarif_ver", sarif_ver);

  let z3_ver  = find(`Z3_VER = "([\d.]+)"`, rawfile, 1);
  rpm.global("z3_ver", z3_ver);

  let z3_glibc  = find(`Z3_X64_GLIBC_VER = "([\d.]+)"`, rawfile, 1);
  rpm.global("z3_glibc", z3_glibc);
}
