%global debug_package %{nil}
%global modulename logitech-trueforce

Name:            dkms-%{modulename}
Version:         0.39.2
Release:         1%{?dist}
Summary:         DKMS kernel driver for Logitech racing wheels (RS50, G PRO, G923)
License:         GPL-2.0-only
URL:             https://github.com/mescon/logitech-trueforce-linux-driver
Source0:         %{url}/archive/refs/tags/v%{version}.tar.gz
Packager:       Luan Oliveira <luanv.oliveira@outlook.com>
ExclusiveArch:  x86_64

Requires:        gcc
Requires:        make
BuildRequires:   sed

Requires:        dkms >= 2.1.0.0
Requires(post):  dkms
Requires(preun): dkms
Requires:        kernel-devel
Requires:        gcc
Requires:        make
Provides:        dkms-logitech-trueforce = %{?epoch:%{epoch}:}%{version}
Requires:        %{modulename}-kmod-common = %{?epoch:%{epoch}:}%{version}
Provides:       dkms-logitech-rs50-linux-driver = 1.0^20260906git.30cacfc-100%{?dist}
Obsoletes:      dkms-logitech-rs50-linux-driver <= 1.0^20260906git.30cacfc-1%{?dist}


%description
dkms-%{modulename} builds and installs the kernel module for the running kernel
%prep
%autosetup -n logitech-trueforce-linux-driver-%{version}

%build
# Nothing to compile here for the DKMS package: DKMS builds the module on
# the target machine. The userspace companions do build here, including
# logi-wheel-gui (the Slint GUI): both openSUSE and Fedora ship a rustc new
# enough for its MSRV, so unlike packaging/debian/rules no version guard
# is needed.

%install
# Module source DKMS compiles, under /usr/src (the .c keeps its historical
# name; Kbuild emits hid-logitech-dd.ko).
install -d %{buildroot}%{_usrsrc}/%{modulename}-%{version}
# dd-lg4ff.c/.h carry the ported classic force-feedback engine for the
# G923 (c266/c267); the Kbuild links it into the same hid-logitech-dd.ko.
install -m 0644 mainline/*.{c,h} mainline/Kbuild mainline/Makefile \
    %{buildroot}%{_usrsrc}/%{modulename}-%{version}/

sed 's/@PKGVER@/%{version}/' packaging/aur/logitech-trueforce-dkms/dkms.conf \
    > %{buildroot}%{_usrsrc}/%{modulename}-%{version}/dkms.conf
echo "v%{version}" > %{buildroot}%{_usrsrc}/%{modulename}-%{version}/.git_hash
# udev rules: hand the wheel's sysfs + hidraw nodes, and /dev/uhid for the
# logi-ffb virtual-device proxy, to the input group. All three ship with
# the driver package.

%files
%license COPYING
%{_usrsrc}/%{modulename}-%{version}/

%post
dkms add -m %{modulename} -v %{version} --rpm_safe_upgrade >/dev/null 2>&1 || :
# Build + install for the running kernel if its headers are present; never
# fail the package install if they are not (the user can build later).
if dkms build -m %{modulename} -v %{version} >/dev/null 2>&1; then
    dkms install -m %{modulename} -v %{version} --force >/dev/null 2>&1 || :
fi

%preun
dkms remove -m %{modulename} -v %{version} --all --rpm_safe_upgrade >/dev/null 2>&1 || true

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
