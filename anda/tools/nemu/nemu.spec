Name:           nemu
Version:        3.5.0
Release:        2%{?dist}
Summary:        Ncurses UI for QEMU

URL:            https://github.com/nemuTUI/nemu
Source:         %{url}/archive/v%{version}.tar.gz
License:        BSD-2-Clause
Packager:       Olivia <git@olivia.sh>

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libgvc)
BuildRequires:  pkgconfig(libcgraph)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libusb)
Requires:       qemu
Requires:       tigervnc

%description
%summary.

%prep
%autosetup 
%cmake -DNM_WITH_NETWORK_MAP=ON -DNM_WITH_DBUS=ON -DNM_WITH_REMOTE=ON -DNM_WITH_USB=ON -DCMAKE_BUILD_TYPE=RelWithDebInfo

%build
%cmake_build

%install
%cmake_install

%files
%doc README.md README_Build.md CONTRIBUTING.md
%license LICENSE
%{_bindir}/nemu
%{_bindir}/ntty
%{_datadir}/%{name}/scripts/*
%{_datadir}/%{name}/templates/config/%{name}.cfg.sample
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_mandir}/man1/nemu.1.*

%pkg_completion -Bz nemu

%changelog
* Sun Jul 19 2026 Olivia <git@olivia.sh> - 3.5.0-2
- Update packager

%autochangelog
