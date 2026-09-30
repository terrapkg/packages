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

  // Z3 is not taken from Ghidra: the spec overrides Ghidra's 4.13.0 pin
  // with 4.13.4, whose Linux arm64 release works.
  // TODO: Restore the Z3_VER lookup once the spec drops that override.
}
