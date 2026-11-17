# stop OOMing
%global rustflags_debuginfo 1

%global proc_macros_commit 7306a90996eaa89284f3e271dbb04152e3eedf96

Name:           taidan
Version:        1.0.3
Release:        2%{?dist}
Summary:        Out-Of-Box-Experience (OOBE) and Welcome App
# https://scancode-licensedb.aboutcode.org/unsplash
SourceLicense:  GPL-3.0-or-later AND GPL-2.0-or-later AND LicenseRef-scancode-unsplash
License:        (%{sourcelicense}) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND Apache-2.0 AND MIT AND (MIT OR Apache-2.0 OR Zlib) AND (0BSD OR MIT OR Apache-2.0) AND BSD-2-Clause AND Zlib AND MIT AND (Apache-2.0 OR GPL-2.0-only) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND GPL-3.0-or-later AND Apache-2.0 AND Unicode-3.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (CC0-1.0 OR Apache-2.0) AND (BSD-3-Clause OR Apache-2.0) AND BSL-1.0 AND ISC AND (GPL-3.0-only OR LicenseRef-Slint-Royalty-free-2.0 OR LicenseRef-Slint-Software-3.0) AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
URL:            https://github.com/Ultramarine-Linux/taidan
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        https://github.com/FyraLabs/rdms_proc_macros/archive/%{proc_macros_commit}/rdms_proc_macros-%{proc_macros_commit}.tar.gz
Packager:       Terra Packaging Team <terra@fyralabs.com>
Obsoletes:      %{name}-default-configs < 1.0.1-2
Requires:       kwin
Requires:       dbus-daemon
Requires:       swaybg
Requires:       polkit >= 126
Requires:       (glib2 or (/usr/bin/plasma-apply-colorscheme and kf6-kconfig))
Requires:       shadow-utils
Requires:       glibc-common
Requires:       util-linux
Requires:       systemd
Requires:       systemd-udev
Requires:       kbd
Requires:       bash
Requires:       (dnf5 and dnf5-command(copr) and dnf5-command(config-manager))
Requires:       flatpak
Recommends:     systemd-homed
Requires:       pciutils
Requires:       mokutil
Requires:       dbus-tools
Requires:       NetworkManager
Requires:       cog
Requires:       acl
Requires:       tzdata
Recommends:     chrony
Recommends:     grubby
Recommends:     xdg-terminal-exec
Requires:       vercel-geist-fonts
Requires:       atkinson-hyperlegible-next-fonts
Requires:       atkinson-hyperlegible-mono-fonts
Requires:       orca
Requires:       /usr/bin/kwriteconfig6
# dlopen()ed by Slint, so not automatic dependencies
Requires:       libxkbcommon
Requires:       libwayland-client
Requires:       libwayland-cursor
Requires:       libwayland-egl
Requires:       libglvnd-egl
BuildRequires:  anda-srpm-macros lld cargo rust-packaging perl systemd-rpm-macros
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libxcrypt)
# read by taidan_proc_macros at build time
BuildRequires:  glibc-all-langpacks
BuildRequires:  xkeyboard-config
BuildRequires:  clang-libs
BuildRequires:  clang-devel

%description
Taidan is a GUI Out-Of-Box-Experience (OOBE) and Welcome App for Ultramarine
Linux, written in Rust and the Slint toolkit.

%prep
%autosetup
rm -rf taidan_proc_macros
mkdir taidan_proc_macros
tar -xzf %{SOURCE1} -C taidan_proc_macros --strip-components=1
%cargo_prep_online

%build
%{cargo_license_online} > LICENSE.dependencies
%cargo_build -- -p taidan -p libtaidan --bin taidan --bin taidan-helper

%install
install -Dpm755 target/rpm/taidan %{buildroot}%{_bindir}/taidan
install -Dpm755 target/rpm/taidan-helper %{buildroot}%{_libexecdir}/taidan-helper
DESTDIR=%buildroot ./scripts/install.sh
rm -rf %buildroot%{_datadir}/taidan/tweaks
install -d %buildroot%{_sharedstatedir}/taidan

%post
%systemd_post taidan-initial-setup.service taidan-initial-setup-reconfiguration.service

%preun
%systemd_preun taidan-initial-setup.service taidan-initial-setup-reconfiguration.service

%postun
%systemd_postun taidan-initial-setup.service taidan-initial-setup-reconfiguration.service

%files
%doc README.md
%license LICENSE.md LICENSE-GPL-2.0-or-later.md LICENSE.dependencies data/avatars/LICENSE.unsplash
%{_bindir}/taidan
%{_libexecdir}/start-taidan
%{_libexecdir}/taidan-helper
%{_datadir}/taidan/polkit/
%config(noreplace) %{_sysconfdir}/pam.d/taidan
%{_sysusersdir}/taidan.conf
%{_unitdir}/taidan-initial-setup.service
%{_unitdir}/taidan-initial-setup-reconfiguration.service
%dir %{_prefix}/lib/taidan/
%dir %{_sharedstatedir}/taidan/
%dir %{_datadir}/taidan/
%{_datadir}/taidan/avatars/
%{_datadir}/taidan/po/
%{_datadir}/taidan/session-config/

%changelog
* Sun Nov 15 2026 Cypress Reed <cypress@fyralabs.com> - 1.0.3-2
- Update packaging for slint rewrite

* Wed Jun 17 2026 madonuko <mado@fyralabs.com> - 0.2.1-2
- split config files to separate subpkg
- remove conflict with initial-setup

* Sun Mar 15 2026 Tulip Blossom <tulilirockz@outlook.com>
- Add dbus-daemon as runtime dependency

* Sun Mar 15 2026 Tulip Blossom <tulilirockz@outlook.com>
- Port manifest from Ultramarine repos to Terra
