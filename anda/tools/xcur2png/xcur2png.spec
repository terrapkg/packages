%global _distro_extra_cflags -Wno-parenthesis -Wno-implicit-int

Name:           xcur2png
Version:        0.7.1
Release:        1%{?dist}
License:        GPL-3.0-or-later
Summary:        Convert X cursors to PNG images
URL:            https://github.com/eworm-de/xcur2png
Source:         %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz
Packager:       Metcya <metcya@gmail.com>

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(xcursor)

%description
xcur2png is a program which let you take PNG image from X cursor, and generate config-file which is reusable by xcursorgen. To put it simply, it is converter from X cursor to PNG image.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS INSTALL NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Sat Dec 13 2025 Metcya <metcya@gmail.com> - 0.7.1
- package xcur2png
