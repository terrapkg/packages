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
BuildRequires:  cmake(minizip-ng)
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(LayerShellQt)
BuildRequires:  pkgconfig(libqalculate)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  wayland-devel
BuildRequires:  nodejs-npm

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

%files
%{_bindir}/%{name}

%changelog
* Fri Dec 26 2025 metcya <metcya@gmail.com> - 0.17.3
- Package vicinae
