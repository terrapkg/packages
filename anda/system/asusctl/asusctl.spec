%global debug_package %{nil}
%global appid org.asus_linux.rog_control_center

Name:           asusctl
Version:        6.3.1
Release:        2%?dist
Epoch:          1
Summary:        A control daemon, CLI tools, and a collection of crates for interacting with ASUS ROG laptops
URL:            https://gitlab.com/asus-linux/asusctl
Source0:        %url/-/archive/%version/asusctl-%version.tar.gz
Source1:        %{appid}.metainfo.xml
License:        MPL-2.0 AND (MIT OR Apache-2.0) AND NCSA AND Unicode-3.0 AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND MIT AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR Zlib) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause (BSD-2-Clause OR Apache-2.0 OR MIT) AND (BSD-3-Clause OR Apache-2.0) AND BSD-3-Clause AND BSL-1.0 AND (CC0-1.0 OR Apache-2.0) AND (GPL-3.0-only OR LicenseRef-Slint-Royalty-free-2.0 OR LicenseRef-Slint-Software-3.0) AND ISC AND MIT AND Zlib AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND Unlicense AND (Zlib OR Apache-2.0 OR MIT)
BuildRequires:  anda-srpm-macros cargo-rpm-macros systemd-rpm-macros mold rust-udev-devel clang-devel
BuildRequires:  desktop-file-utils
BuildRequires:  cmake
BuildRequires:  rust
BuildRequires:  rust-std-static
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(fontconfig)
ExclusiveArch:  x86_64

Packager:       Metcya <metcya@gmail.com>

%description
%summary.

%package rog-gui
Summary:    An experimental gui for %name
Requires:   %name
Provides:   rog-control-center
Provides:   rog-gui

%description rog-gui
A one-stop-shop GUI tool for asusd/asusctl. It aims to provide most controls,
a notification service, and ability to run in the background.

%prep
%autosetup -n asusctl-%version
%cargo_prep_online

%build
%cargo_build

%install
%make_install

install -D -m 0644 README.md %{buildroot}/%{_docdir}/%{name}/README.md
install -D -m 0644 rog-anime/README.md %{buildroot}/%{_docdir}/%{name}/README-anime.md
install -D -m 0644 rog-anime/data/diagonal-template.png %{buildroot}/%{_docdir}/%{name}/diagonal-template.png
%terra_appstream -o %{S:1}

%{cargo_license_online} > LICENSE.dependencies

desktop-file-validate %{buildroot}/%{_datadir}/applications/rog-control-center.desktop

%files
%license LICENSE
%license LICENSE.dependencies
%{_datadir}/asusctl/LICENSE
%{_bindir}/asusd
%{_bindir}/asusd-user
%{_bindir}/asusctl
%{_unitdir}/asusd.service
%{_userunitdir}/asusd-user.service
%{_udevrulesdir}/99-asusd.rules
%dnl %{_sysconfdir}/asusd/
%{_datadir}/asusd/aura_support.ron
%{_datadir}/dbus-1/system.d/asusd.conf
%{_datadir}/icons/hicolor/512x512/apps/asus_notif_yellow.png
%{_datadir}/icons/hicolor/512x512/apps/asus_notif_green.png
%{_datadir}/icons/hicolor/512x512/apps/asus_notif_red.png
%{_datadir}/icons/hicolor/512x512/apps/asus_notif_blue.png
%{_datadir}/icons/hicolor/512x512/apps/asus_notif_orange.png
%{_datadir}/icons/hicolor/512x512/apps/asus_notif_white.png
%{_datadir}/icons/hicolor/scalable/status/gpu-compute.svg
%{_datadir}/icons/hicolor/scalable/status/gpu-hybrid.svg
%{_datadir}/icons/hicolor/scalable/status/gpu-integrated.svg
%{_datadir}/icons/hicolor/scalable/status/gpu-nvidia.svg
%{_datadir}/icons/hicolor/scalable/status/gpu-vfio.svg
%{_datadir}/icons/hicolor/scalable/status/notification-reboot.svg
%{_docdir}/%{name}/
%{_datadir}/asusd/

%post
%systemd_post asusd.service
%systemd_user_post asusd-user.service

%preun
%systemd_preun asusd.service
%systemd_user_preun asusd-user.service

%postun
%systemd_postun_with_restart asusd.service
%systemd_user_postun_with_restart asusd-user.service

%files rog-gui
%{_bindir}/rog-control-center
%{_datadir}/applications/rog-control-center.desktop
%{_datadir}/icons/hicolor/512x512/apps/rog-control-center.png
%{_datadir}/rog-gui
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Fri Jan 16 2026 metcya <metcya@gmail.com> - 6.3.0-2
- Update ROG Control Center metainfo

* Tue Jan 13 2026 Owen Zimmerman <owen@fyralabs.com> - 6.2.0-3
- Add dependency licenses

* Tue Dec 9 2025 Metcya <metcya@gmail.com> - 6.2.0
- Add metainfo

* Mon Dec 1 2025 Metcya <metcya@gmail.com>
- Add systemd scriptlets

* Tue Nov 18 2025 Metcya <metcya@gmail.com>
- Remove unnecessary patch

* Sun Oct 26 2025 Metcya <metcya@gmail.com>
- Package asusctl
