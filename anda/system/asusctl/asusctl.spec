%global debug_package %{nil}
%global appid org.asus_linux.rog_control_center

Name:           asusctl
Version:        6.2.0
Release:        2%?dist
Summary:        A control daemon, CLI tools, and a collection of crates for interacting with ASUS ROG laptops
URL:            https://gitlab.com/asus-linux/asusctl
Source0:        %url/-/archive/%version/asusctl-%version.tar.gz
Source1:        %{appid}.metainfo.xml
License:        MPL-2.0
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

desktop-file-validate %{buildroot}/%{_datadir}/applications/rog-control-center.desktop

%files
%license LICENSE
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
* Tue Dec 9 2025 Metcya <metcya@gmail.com> - 6.2.0
- Add metainfo

* Mon Dec 1 2025 Metcya <metcya@gmail.com>
- Add systemd scriptlets

* Tue Nov 18 2025 Metcya <metcya@gmail.com>
- Remove unnecessary patch

* Sun Oct 26 2025 Metcya <metcya@gmail.com>
- Package asusctl
