Name:           vicinae
Version:        0.20.1
Release:        1%?dist
License:        GPL-3.0
URL:            https://docs.vicinae.com
Source:         https://github.com/vicinaehq/%{name}/archive/refs/tags/v%{version}.tar.gz
Summary:        A high-performance, native launcher for Linux
Packager:       metcya <metcya@gmail.com>

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(absl)
BuildRequires:  openssl-devel
BuildRequires:  cmark-gfm-devel
BuildRequires:  cmake(glaze)
BuildRequires:  cmake(minizip)
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(LayerShellQt)
BuildRequires:  pkgconfig(libqalculate)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  wayland-devel
BuildRequires:  nodejs-npm
BuildRequires:  systemd-rpm-macros
BuildRequires:  anda-srpm-macros
BuildRequires:  ninja-build
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  desktop-file-utils

Requires:       nodejs-npm

%description
Vicinae (pronounced "vih-SIN-ay") is a high-performance, native launcher for
your desktop — built with C++ and Qt.

%prep
%autosetup

%build
%cmake -G Ninja -DCMAKE_BUILD_TYPE=None -DBUILD_SHARED_LIBS=OFF -DNOSTRIP=ON
%cmake_build

%install
%cmake_install
install -Dm 644 extra/%{name}.desktop -t %{buildroot}%{_appsdir}
install -Dm 644 extra/%{name}-url-handler.desktop -t %{buildroot}%{_appsdir}
%desktop_file_edit -k StartupWMClass -v vicinae-server -f %{buildroot}%{_appsdir}/%{name}.desktop

%check
%desktop_file_validate -f %{buildroot}%{_appsdir}/%{name}.desktop

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun_with_restart %{name}.service

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_userunitdir}/%{name}.service
%{_datadir}/%{name}/themes/
%{_appsdir}/%{name}.desktop
%{_appsdir}/%{name}-url-handler.desktop
%{_hicolordir}/512x512/apps/%{name}.png
%{_sysconfdir}/chromium/native-messaging-hosts/com.vicinae.vicinae.json
%{_prefix}/lib/mozilla/native-messaging-hosts/com.vicinae.vicinae.json
%{_datadir}/%{name}/native-messaging-hosts/com.vicinae.vicinae.chromium.json.in
%{_datadir}/%{name}/native-messaging-hosts/com.vicinae.vicinae.firefox.json.in
%{_libexecdir}/%{name}/vicinae-browser-link
%{_libexecdir}/%{name}/vicinae-data-control-server
%{_libexecdir}/%{name}/vicinae-server
%{_libexecdir}/%{name}/vicinae-snippet-server

%changelog
* Wed Feb 18 2026 Jaiden Riordan <jade@fyralabs.com> - 0.19.8
- Fixup desktop file and xdgpp
* Fri Dec 26 2025 metcya <metcya@gmail.com> - 0.17.3
- Package vicinae