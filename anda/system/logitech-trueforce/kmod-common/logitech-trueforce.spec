Name:           logitech-trueforce
Version:        0.39.2
Release:        1%{?dist}
Summary:        kernel driver for Logitech racing wheels (RS50, G PRO, G923)
License:        GPL-2.0-only
URL:            https://github.com/mescon/logitech-trueforce-linux-driver
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        com.github.logitech-trueforce-linux-driver.metainfo.xml
Packager:       Luan Oliveira <luanv.oliveira@outlook.com>

BuildArch:      noarch
BuildRequires:  systemd-rpm-macros

# The pre-split package pulled the userspace tools in hard; recommending
# logi-wheel keeps "install the driver, get the ecosystem" while still
# allowing a lean module-only install.
Recommends:     logi-wheel
# Switches an Xbox edition (G923 c26d, RS50 c275) into PC mode (c26e, c276) on plug-in;
# the udev rule that runs it is a no-op without the binary present.
Recommends:     usb_modeswitch

# select right build mode depending on whether akmods or dkms is already installed
Requires: ((%{name}-kmod = %{?epoch:%{epoch}:}%{version}) if akmods)
Requires: ((dkms-%{name} = %{?epoch:%{epoch}:}%{version}) if dkms)
Requires: ((%{name}-kmod = %{?epoch:%{epoch}:}%{version}) or (dkms-%{name} = %{?epoch:%{epoch}:}%{version}))

Provides:       %{name}-kmod-common = %{?epoch:%{epoch}:}%{version}

Provides:       logitech-rs50-linux-driver = 1.0^20260904git.320bf50-100%{?dist}
Provides:       logitech-rs50-linux-driver-kmod-common = 1.0^20260904git.320bf50-100%{?dist}
Provides:       akmod-logitech-rs50-linux-driver = 1.0^20260904git.320bf50-100%{?dist}
Provides:       dkms-logitech-rs50-linux-driver = 1.0^20260904git.320bf50-100%{?dist}
Obsoletes:      logitech-rs50-linux-driver <= 1.0^20260904git.320bf50-1%{?dist}
Obsoletes:      logitech-rs50-linux-driver-kmod-common <= 1.0^20260904git.320bf50-1%{?dist}
Obsoletes:      dkms-logitech-rs50-linux-driver <= 1.0^20260904git.320bf50-1%{?dist}
Obsoletes:      akmod-logitech-rs50-linux-driver <= 1.0^20260904git.320bf50-1%{?dist}

%description
Force feedback, TrueForce texture routing, and G HUB-equivalent settings
exposed through sysfs for the Logitech RS50 and G PRO direct-drive racing
wheels. DKMS builds and installs the module (hid-logitech-dd) for the running
kernel and rebuilds it on kernel upgrades.

The module is scoped to the direct-drive wheel USB IDs (c276 RS50 native, c272
G PRO Xbox/PC and RS50 compat, c268 G PRO PS/PC) and coexists with the in-tree
hid-logitech-hidpp driver, which continues to serve every other Logitech
device, so no blacklist is needed.

TrueForce in Proton sims additionally needs Logitech's proprietary signed SDK
DLLs, which are not shipped by this package; see the bundled Getting Started
guide

%prep
%autosetup -n logitech-trueforce-linux-driver-%{version}

%build

%install
# udev rules: hand the wheel's sysfs + hidraw nodes, and /dev/uhid for the
# logi-ffb virtual-device proxy, to the input group. All three ship with
# the driver package.
install -D -m 0644 udev/70-logitech-trueforce.rules \
    %{buildroot}%{_prefix}/lib/udev/rules.d/70-logitech-trueforce.rules
install -D -m 0644 udev/71-logi-ffb-uhid.rules \
    %{buildroot}%{_prefix}/lib/udev/rules.d/71-logi-ffb-uhid.rules
# G923 (c266/c267/c26e) driver pre-emption: PID-scoped rebind rule plus a
# softdep/blacklist hint (see the file for why the fork blacklist is safe).
install -D -m 0644 udev/72-logitech-g923-rebind.rules \
    %{buildroot}%{_prefix}/lib/udev/rules.d/72-logitech-g923-rebind.rules
# Xbox editions (G923 c26d, RS50 c275) boot-mode switch: needs usb_modeswitch
# (Recommends above), a no-op without it.
install -D -m 0644 udev/73-logitech-xbox-modeswitch.rules \
    %{buildroot}%{_prefix}/lib/udev/rules.d/73-logitech-xbox-modeswitch.rules
install -D -m 0644 packaging/modprobe.d/hid-logitech-dd.conf \
    %{buildroot}%{_sysconfdir}/modprobe.d/hid-logitech-dd.conf

install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo/com.github.logitech-trueforce-linux-driver.metainfo.xml

%files
%license COPYING
%doc README.md
%{_prefix}/lib/udev/rules.d/70-logitech-trueforce.rules
%{_prefix}/lib/udev/rules.d/71-logi-ffb-uhid.rules
%{_prefix}/lib/udev/rules.d/72-logitech-g923-rebind.rules
%{_prefix}/lib/udev/rules.d/73-logitech-xbox-modeswitch.rules
%config(noreplace) %{_sysconfdir}/modprobe.d/hid-logitech-dd.conf
%{_datadir}/metainfo/com.github.logitech-trueforce-linux-driver.metainfo.xml


%changelog
* Wed Sep 2 2026 luan Oliveira <luanv.oliveira@outlook.com> - 0.39.2-1
- ported to terra

* Sun Jul 26 2026 mescon <5875228+mescon@users.noreply.github.com> - 0.20.0-1
- Renamed the userspace subpackages: logi-dd -> logi-wheel, logi-dd-gui ->
  logi-wheel-gui ("dd" meant direct-drive, but the app now also covers the
  gear-driven G923). Provides/Obsoletes on the old names move existing
  installs over automatically.

* Mon Jul 20 2026 mescon <5875228+mescon@users.noreply.github.com> - 0.16.1-1
- Build the Rust workspace offline against vendored crate dependencies
  (new Source1 tarball produced by the publish workflow): OBS builders
  have no network access, so the previous cargo build failed to resolve
  index.crates.io and the repository kept serving stale binaries.

* Sat Jul 18 2026 mescon <5875228+mescon@users.noreply.github.com> - 0.15.0-1
- Ship the userspace ecosystem as layered subpackages: logi-dd (settings
  TUI, logi-ffb DirectInput force-feedback proxy, logi-tf-sim
  simulated-TrueForce daemon, and the TrueForce SDK shim installer;
  requires the driver package, which now carries both udev rules) and
  logi-dd-gui (graphical settings app, GPL-3.0-or-later, with desktop
  entry, icon, and the GUI's windowing/rendering runtime dependencies;
  requires logi-dd). Built from the userspace/logi-dd Rust workspace.
