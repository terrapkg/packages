Name:       ueberzugpp
Version:    2.9.10
Release:    3%{?dist}
License:    GPL-3.0-or-later
Summary:    Drop in replacement for ueberzug written in C++ 
URL:        https://github.com/jstkdng/%{name}
Source:     %{url}/archive/v%{version}.tar.gz
Packager:   Olivia <git@olivia.sh>

BuildRequires:  cmake
BuildRequires:  gcc-c++ 
BuildRequires:  pkgconfig(vips)
BuildRequires:  pkgconfig(libsixel)
BuildRequires:  pkgconfig(chafa)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(tbb)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  cli11-devel
BuildRequires:  pkgconfig(spdlog)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  range-v3-devel
BuildRequires:  pkgconfig(opencv)
BuildRequires:  xcb-util-image-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  extra-cmake-modules

%description
Überzug++ is a command line utility written in C++ which allows to draw images
on terminals by using X11/wayland child windows, sixels, kitty and iterm2.

%prep
%autosetup

%conf
%cmake . -DENABLE_WAYLAND=ON    \
         -DENABLE_XCB_ERROR=ON

%build
%cmake_build

%install
%cmake_install

%files
%doc README.md
%doc CODE_OF_CONDUCT.md
%license LICENSE
%{_bindir}/ueberzug
%{_bindir}/ueberzugpp
%{_mandir}/man1/ueberzug.1*
%{_mandir}/man1/ueberzugpp.1*

%check
%ctest

%changelog
* Sun Jul 19 2026 Olivia <git@olivia.sh> - 2.9.10-3
- Update packager

* Tue Nov 11 2025 Olivia <git@olivia.sh>
- Package ueberzugpp
