Name:           vicinae
Version:        0.17.3
Release:        1%{?dist}
License:        GPL-3.0
URL:            https://docs.vicinae.com
Source:         https://github.com/vicinaehq/%{name}/archive/refs/tags/v%{version}.tar.gz
Summary:        a high-performance, native launcher for Linux
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
BuildRequires:  wayland-devel
BuildRequires:  nodejs-npm
BuildRequires:  systemd-srpm-macros

%description
Vicinae (pronounced "vih-SIN-ay") is a high-performance, native launcher for
your desktop — built with C++ and Qt.

%prep
%autosetup

%build
%cmake -DNOSTRIP=ON
%cmake_build

%install
%cmake_install
install -Dm 644 extras/%{name}.desktop -t %{buildroot}%{_datadir}/applications
install -Dm 644 extras/%{name}-url-handler.desktop -t %{buildroot}%{_datadir}/applications

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun_with_restart %{name}.service

%files
%{_bindir}/%{name}
%{_userunitdir}/%{name}.service
%{_datadir/%{name}/themes/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-url-handler.desktop
%{_hicolordir}/512x512/apps/%{name}.png

%changelog
* Fri Dec 26 2025 metcya <metcya@gmail.com> - 0.17.3
- Package vicinae
