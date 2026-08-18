%define debug_package %nil
%global ver 2017-a

Name:           man-pages-posix
Version:        %(echo %ver | sed 's/-/./g')
Release:        1%?dist
Summary:        POSIX.1-2017 man pages (pages in sections except 0p, 1p, and 3p)
License:        LicenseRef-IEEE-2017
URL:            https://www.kernel.org/doc/man-pages/
Source0:        https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/man-pages-posix/man-pages-posix-%ver.tar.xz
Packager:       madonuko <mado@fyralabs.com>
BuildRequires:  make
BuildArch:      noarch

%description
This package contains the POSIX.1-2017 man pages (pages in sections except 0p, 1p, and 3p).

%prep
%autosetup -n %name-2017

%build

%install
%make_install MANDIR=%_mandir

%files
%doc README
%license POSIX-COPYRIGHT
%_mandir/man0p/*
%_mandir/man1p/*
%_mandir/man3p/*

%changelog
* Tue Aug 18 2026 madonuko <mado@fyralabs.com> - 2017.a-1
- Initial package
