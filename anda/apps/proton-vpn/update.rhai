import "andax/spec.rhai" as spec;

rpm.global("metainfo_commit", gh_commit("flathub/com.protonvpn.www"));
if rpm.changed() {
  let rel = spec::get_release(rpm).parse_int();
  rpm.release(rel + 1);
}

rpm.version(gh_tag("ProtonVPN/proton-vpn-gtk-app"));
