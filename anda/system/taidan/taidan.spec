Name:           taidan
Version:        0.2.0
Release:        1%{?dist}
Summary:        Out-Of-Box-Experience (OOBE) and Welcome App
SourceLicense:  GPL-3.0-or-later AND GPL-2.0-or-later
License:        (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND Unicode-3.0 AND (Unlicense OR MIT) AND Zlib AND GPL-3.0-or-later AND GPL-2.0-or-later
URL:            https://github.com/Ultramarine-Linux/taidan
Packager:       Terra Packaging Team <terra@fyralabs.com>
Conflicts:      initial-setup
Requires:       dbus-daemon
Requires:       (glib2 or (/usr/bin/plasma-apply-colorscheme and kf6-kconfig))
Requires:       shadow-utils
Requires:       systemd-udev
Requires:       bash
Requires:       (dnf5 and dnf5-command(copr))
Requires:       flatpak
Requires:       libwebp
Requires:       webp-pixbuf-loader
Requires:       xhost
Requires:       kwin-wayland swaybg
Requires:       netto network-manager-applet
Requires:       polkit
BuildRequires:  anda-srpm-macros mold cargo rust-packaging perl systemd-rpm-macros
BuildRequires:  pkgconfig(libhelium-1)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  gcc clang clang-libs
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libattr)
BuildRequires:  glibc-all-langpacks

%description
Taidan is a GUI Out-Of-Box-Experience (OOBE) and Welcome App for Ultramarine
Linux, written in Rust and the Helium toolkit.

%prep
%git_clone
%cargo_prep_online

%build
%{cargo_license_online} > LICENSE.dependencies

%install
%cargo_install
DESTDIR=%buildroot ./scripts/install.sh

%files
%doc README.md
%license LICENSE.md LICENSE.dependencies
%_bindir/taidan
%_libexecdir/start-taidan
%_datadir/polkit-1/rules.d/100-taidan.rules
%_datadir/taidan/
%_presetdir/95-taidan.preset
%_sysconfdir/com.fyralabs.Taidan/
%_sysconfdir/pam.d/taidan
%_sysusersdir/taidan.conf
%_unitdir/taidan-initial-setup.service
%_unitdir/taidan-initial-setup-reconfiguration.service
%dir %_prefix/lib/taidan/
%_prefix/lib/taidan/labwc/*

%changelog
* Sun Mar 15 2026 Tulip Blossom <tulilirockz@outlook.com>
- Add dbus-daemon as runtime dependency

* Sun Mar 15 2026 Tulip Blossom <tulilirockz@outlook.com>
- Port manifest from Ultramarine repos to Terra
